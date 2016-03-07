def ter(a, b):
    list_a = []
    for j in b:
        for i in a:
            print "i=",i, " and j=",j
            list_a.append(i)
            if i == j:
                n = a.index(i)
                print "n=",n
                print a
#                list_a.append(i)
                print 'list', list_a
                list_a.pop(n)
            print a
    return list_a

    

#  for item in set(L).difference(L2)

'''
example:
def fib(n):
    a = b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b
'''

'''
for item in set(L).difference(L2)
'''
