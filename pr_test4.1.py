# palindrom
import sys
inp_string = str(sys.argv[1])

print inp_string

change = inp_string[::-1]
print change

if inp_string == change:
    print "YES"
else: print "NO"
