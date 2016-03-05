def counter(a, b):
    counter = 0
    for i in b:
        print (a, 'in', int(i))
        if a == int(i):
            counter += 1
    return counter




'''
def fib(n):
    a = b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b
'''
