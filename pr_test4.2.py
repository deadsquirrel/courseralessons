#input:  padawan young my HAVE MUST YOU PATIENCE
#result: PATIENCE YOU MUST HAVE my young padawan
import sys
sen = str()
sent = str()
inp = sys.argv[1]

for i in inp:
    if i != "[" and i != "]" and i != "'" and i !=",":
        sen = sen + i

inp_sp = sen.split()
for i in inp_sp:
    sen = i + " " + sen
print sen.strip()
