# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.

fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
summ = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    position = line.find(":")
    poss = line[position+1:] 
    inp = float(poss.strip())
    summ = summ + inp
    print inp, summ
print "Average spam confidence: ", summ/ count

