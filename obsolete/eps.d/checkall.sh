#!/bin/sh
# vim:set ts=8 sts=2 sw=2 tw=0:
#
# Last Change:	25-Jan-2004.
# Maintainer:	MURAOKA Taro <koron@tka.att.ne.jp>

for dir in `cat datadirs` ; do
  if test -d $dir ; then
    echo "Checking for $dir"
    perl ./eolcheck.pl $dir/*.eps
  fi
done
