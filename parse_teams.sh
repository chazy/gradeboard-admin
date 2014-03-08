#!/bin/bash
# 
# for posterity... shouldn't be needed anymore
# (probably can use os1.group-foreach easier than these files)

E=`which echo`

TEAM_CSV=${1:-teams.csv}
OUT_TEAM_LIST=${2:-team_list}
OUT_STUD_LIST=${3:-students}

$E "" > $OUT_TEAM_LIST
$E "" > $OUT_STUD_LIST

cat $TEAM_CSV | (
while read line; do
	T=`echo $line | awk -F ',' '{print $1}'`
	T=${T// /}
	T=${T//\"/}
	U=`echo $line | awk -F ',' '{print $3}'`
	U=${U// /}
	U=${U//\"/}
	if [ ! "x$T" = "x" ]; then
		TEAM=$T
		$E "Team: '$TEAM'"
		$E >> $OUT_TEAM_LIST
		$E -n "$TEAM " >> $OUT_TEAM_LIST
	fi
	if [ ! "x$U" = "x" ]; then
		UNI=$U
		$E "    $TEAM member: $UNI"
		$E -n "$UNI," >> $OUT_TEAM_LIST
		$E $UNI >> $OUT_STUD_LIST
	fi
done
)
