import sys
inp_list = sys.argv[1]
#inp_list = [9,6,6,4,4,30]
t_list = []
last_list = []
next_list = []

print "inp:",inp_list
print "out0:",t_list
for i in inp_list:
    if i.isdigit():
        t_list.append(i)
print t_list
#index = 0
for c, i in enumerate(t_list):
    print "-------------------for---1------"
 #   print "index: ", index 
    print "i: ", i , "c: ", c
#    new_list = t_list[index+1:]
    new_list = t_list[c+1:]
    print "new_list:", new_list 
    for count, j in enumerate(new_list):
        print "-----for---2------"
        print "count: ", count, "j: ", j 
        if j == i:
            print j, " ==  ", i
            t_list.pop(count+1)
#            last_list.append(i)
        else:
            print "j:",j,"i: ", i

    print "================== "
print " t_list:", t_list

