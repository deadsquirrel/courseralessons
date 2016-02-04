import sys
sen = str()
sent = str()
inp = str(sys.argv[1:])

for i in inp:
    if i == "[" or i == "]" or i == "'" or i ==",":
        continue
    else:
        sen = sen + i

inp_sp = sen.split()

for i in inp_sp:
    sent = i + " " + sent
print sent.strip()


