# Use words.txt as the file name
fname = raw_input("Enter file name: ")
print fname
fh = open(fname)

for line in fh:
    line = line.strip()
    print line.upper()

