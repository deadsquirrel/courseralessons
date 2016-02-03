# palindrom
import sys
inp_string = str(sys.argv[1])
#r = None
print inp_string
#y = len (inp_string)

inp = inp_string.lower()
inp_string = inp.replace(" ", "")

print "Out:",inp_string
    
    
#print inp_string.replace("w", "vv")


change = inp_string[::-1]
print change

if inp_string == change:
    print "YES"
else: print "NO"


