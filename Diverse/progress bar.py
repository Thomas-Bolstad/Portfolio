#Progress Bar

import sys, time, os
orig = "[----------]"


for i in range(1, 101):
    posB = (i - i % 10)/10
    posS = i % 10
    newstring = orig[0] + posS*"x" + orig[posS + 1: 12]
    newstring = newstring[0] + posB*"X" + newstring[posB + 1: 12]
    time.sleep(0.05)
    sys.stdout.write("%07s\b\b\b\b\b\b\b\b\b\b\b\b" % newstring)
    sys.stdout.flush()
