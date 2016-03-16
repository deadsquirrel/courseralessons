import sys
inp_list = sys.argv[1]
#'55668978'
count = 0

print "list:",inp_list

for i in inp_list:
    print i
    if i.isdigit():
        if int(i) == 9:
            count += 1
        elif int(i) == 6:
            count += 1
        elif int(i) == 0:
            count += 1
        elif int(i) == 4:
            count += 1
        elif int(i) == 8:
            count += 2
        else:
            continue
    else:
        print "not digit! next i"
        continue
    print "================== "
print "count hole of list:", count



