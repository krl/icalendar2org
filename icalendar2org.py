#!/usr/bin/python
import sys
from vobject import iCalendar, readOne

for x in readOne(sys.stdin).getChildren():
    if x.name == "VEVENT":
        print "* [[" + x.url.value + "][" + x.summary.value + "]]"
        print "SCHEDULED: " + x.dtstart.value.strftime("<%Y-%m-%d %a>")
        print x.description.value
