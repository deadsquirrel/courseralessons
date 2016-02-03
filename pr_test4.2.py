#input:  padawan young my HAVE MUST YOU PATIENCE
#result: PATIENCE YOU MUST HAVE my young padawan
import sys
sen = str()
inp = sys.argv[1]
inp_sp = inp.split()
for i in inp_sp:
    sen = i + " " + sen
print sen.strip()
