import sys
inp_list = sys.argv[1]
#inp_list = [9,6,6,4,4,30]
t_list = []
w_list = []
next_list = []

print "inp:",inp_list
print "out0:",t_list
for i in inp_list:
    if i.isdigit():
        t_list.append(i)
print t_list
index = 0
for i in t_list:
    print "-----for---1------"
    print "index: ", index 
    print "i: ", i 
    new_list = t_list[index+1:]
    print "new_list:", new_list 
    for j in new_list:
        print "-----for---2------"
        print "j: ", j 
 #       w_list.append(j)
 #       print "w_list:", w_list 
        if j == i:
            t_list.remove(t_list[index+1]) 
            print "1 j:",j,"i: ", i
        else:
            print "2 j:",j,"i: ", i
    index += 1
    print "================== "
print "--------------"
#print "qq w_list:", w_list
print "rr t_list:", t_list
