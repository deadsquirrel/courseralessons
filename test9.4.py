fname = raw_input("Enter file name: ")

fh = open(fname)
counts = dict()
maxv = 0

for line in fh:
    if not line.startswith('From '): continue
    str = line.split()
    name = str[1]
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
    for val in counts.values():
        if val > maxv:
            maxv = val

print name, maxv  

