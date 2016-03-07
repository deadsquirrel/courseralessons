def ter(a, b):
    list = []
    for j in b:
        for i in a:
            print "i=",i, " and j=",j
            if i == j:
                n = a.index(i)
                print "n=",n
                print a
                print 'list', list.append(i)
                c = list.pop(n)
            print a
    return list

    

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
