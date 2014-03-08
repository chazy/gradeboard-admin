GradeBoard Admin Tools
======================
This is a set of admin tools for managing Git and Review Board in a teaching
setting, see http://www.cs.columbia.edu/~cdall/pubs/fp1078-dall.pdf for more
info.

The overall design idea is that this management repo is cloned for each year in
which it is used, downloaded by an administrative instructor to his/her own
computer, and is configured to interact remote with the course server, always
running locally from the instructor's computer.


Known Issues
============
These tools were originally written to work with gitosis (now deprecated and
succeeded by gitolite) and may need to be tweaked for a more update Git hosting
configuration.

Further, at Columbia University, for which this tool was originally developed,
student IDs are always the part of their e-mail addresses preceding the '@'.
This may need to be tweaked as well.

License
=======
This software is licensed under GPLv3.  See COPYRIGHT and LICENSE for more info.
