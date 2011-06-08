#!/usr/bin/python
# -*- mode: Python; encoding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

import sys
from vobject import iCalendar, readOne

for x in readOne(sys.stdin).getChildren():
    if x.name == "VEVENT":

        print "* {}\nSCHEDULED: {}\n[[{}][link]]\n{}"\
            .format(x.summary.value.encode("utf-8"),
                    x.dtstart.value.strftime("<%Y-%m-%d %a>"),
                    x.url.value,
                    x.description.value.encode("utf-8"))
