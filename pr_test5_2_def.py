def counter(a, b):
    counter = 0
    for i in b:
        for j in a:
            print (int(j), 'in', int(i))
            if int(j) == int(i):
                counter += 1
                print "N", counter
    return counter




'''
example:
def fib(n):
    a = b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b
'''
