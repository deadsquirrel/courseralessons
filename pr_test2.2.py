import math
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])
text = "la"
string = ""
count = 1


if x == 0:
    print "Error! x = 0"
elif z > 1:
    print "Error! z > 1"
elif y== 0:
    if z == 1:
        print "Everybody sing a song:!"
    else: print "Everybody sing a song:."
else:
    while count < x:
        string = string + text + "-"
        count = count + 1
    string = string + text
    song = (y-1)*(string +" ") + string
    if z == 1:
        print "Everybody sing a song:",song +"!"
    else: print "Everybody sing a song:",song+"."
