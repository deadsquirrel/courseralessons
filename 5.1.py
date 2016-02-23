import sys
inp_list = sys.argv[1]
#inp_list = [9,6,6,4,4,30]
out_list = []
next_list = []

print "inp:",inp_list
print "out0:",out_list
for i in inp_list:
    if i.isdigit():
        out_list.append(i)
print out_list
for i in out_list:
    new_list = out_list[int(i):]
    for j in new_list:
        if i == j:
            new_list = out_list.remove(j) 

print new_list
'''
    if i != j:
        print i, j, "a"
    else: print "b"
    #   next_list.append(i)
        
print next_list
'''

'''
print "inp:",inp_list
print "out0:",out_list
for i in inp_list:
    if i.isdigit():
        out_list.append(i)
print out_list
'''
