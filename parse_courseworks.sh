#!/bin/bash
#
# parse_courseworks.sh
# Christoffer Dall
# Fall 2011
#
# Parse the output from courseworks into the expected format
# Expects the following format:
#
# ^LastName, FirstNames (uni)\s*$
#

. `dirname $(which $(test -L $0 && readlink $0 || echo $0))`/os1.cfg
[[ $# == 1 ]] || os1error "Usage '$0 file'"

SRC="$1"
if [ ! -f ]; then
	echo "error: '$1' could not be opened"
	exit 1
fi
TMP_FILE=/tmp/__class_list.tmp
echo -n > $TMP_FILE

cat $SRC | (
while read line; do
	line=`echo $line | sed 's/\(.*\), \(.*\) (\(.*\)).*$/\2 \1 (\3@columbia.edu)/'`
	echo $line >> $TMP_FILE
done
)

sort "$TMP_FILE" -o "$SRC"
