#!/usr/bin/python

import io
import sys
import os
import logging
import re

UNI_REGEX = '\((\w+)@columbia\.edu\)'


class OSClass:
    students = []
    teams = {}
    cvn_students = []

    def __init__(self, students_file=None, team_file=None, cvn_file=None):
        # Students file
        if students_file:
            regex = re.compile(UNI_REGEX)
            file = open(students_file, "r")
            try:
                while 1:
                    line = file.readline()
                    if not line:
                        break

                    m = regex.search(line)
                    self.students.append(m.group(1).lower().strip())
            except:
                logging.exception("something went wrong")
                return
            finally:
                file.close()

        # Teams file
        if team_file:
            file = open(team_file, "r")
            try:
                while 1:
                    line = file.readline()
                    if not line:
                        break
                    toks = line.split(' ')
                    team = toks[0]
                    members = toks[1].split(',')
                    for member in members:
                        self.add_member(team, member.lower().strip())
            except:
                logging.exception("something went wrong")
                return
            finally:
                file.close()

        # CVN file
        if cvn_file:
            file = open(cvn_file, "r")
            try:
                while 1:
                    line = file.readline()
                    if not line:
                        break
                    self.cvn_students.append(line.strip().lower())
            except:
                logging.exception("something went wrong")
                return
            finally:
                file.close()

    def is_cvn(self, student):
        return (student in self.cvn_students)

    def add_member(self, team, member):
        if team in self.teams.keys():
            self.teams[team].append(member.lower().strip())
        else:
            self.teams[team] = [member.lower().strip()]


def check_dupes():
    osclass = OSClass(team_file="team_list")

    for team,members in osclass.teams.iteritems():
        for lt, lms in osclass.teams.iteritems():
            for member in members:
                if member in lms and team != lt:
                    print "Duplicate member %s found in %s and %s" % (member, team, lt)


def check_missing():
    osclass = OSClass(students_file="class_list", team_file="team_list",
            cvn_file="cvn_list")
    missing = []
    missing_cvn = []
    zombies = []
    for uni in osclass.students:
        found = False
        for team,members in osclass.teams.iteritems():
            if uni in members:
                found = True
                break
        if not found:
            if osclass.is_cvn(uni):
                missing_cvn.append(uni)
            else:
                missing.append(uni)

    for team,members in osclass.teams.iteritems():
        for member in members:
            if not member in osclass.students:
                zombies.append(member)

    if missing:
        print "Missing students:"
    for m in missing:
        print "  Missing assignment for %s" % (m)

    if missing_cvn:
        print "\nMissing CVN students:"
    for m in missing_cvn:
        print "Missing assignment for %s" % (m)

    if zombies:
        print "Zombie students:"
    for m in zombies:
        print "  %s is a zombie" % (m)

    dropped_students = []
    for team,members in osclass.teams.iteritems():
        for m in members:
            if not m in osclass.students:
                dropped_students.append((m, team))
    if dropped_students:
        print "\nDropped students still in teams:"
    for tup in dropped_students:
        print "Student %s dropped, still in team %s" % tup


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage %s dup|mis" % (sys.argv[0])
        exit(1)

    if sys.argv[1] == 'dup':
        check_dupes()
    else:
        check_missing()
