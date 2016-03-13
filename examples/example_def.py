'''
n = 100
for x in range(n):
    is_cool = x < 10 or (x / 10 == x % 10)
    print x, is_cool
'''
#or

def check_if_is_cool(number):
    is_cool = number < 10 or (number / 10 == number % 10)
    print number, is_cool

n = 100
for x in range(n):
    check_if_is_cool(x)

    
#or

def is_cool(number): # limited by 0 <= number <= 99
    return number < 10 or (int(number) / 10 == number % 10)

n = 100
for x in range(n):
    print x, is_cool(x)

#---
    
def has_dividable_11_2_before_n(n = 99):

    
print has_dividable_11_2_before_n()

#---

def is_dividable(x, dividers = [11, 2]):
    for divider in dividers:
        if x % divider != 0:
            return False
    return True

def has_dividable_numbers(n = 99, dividers = [11, 2]):
    for i in range(n):
        if is_dividable(i+1, dividers):
            return True
    return False

n = int(raw_input('input N:'))
print "11, 2 : " + str(has_dividable_numbers(n))
print "5 : " + str(has_dividable_numbers(n, [5]))
print "2, 3, 5 : " + str(has_dividable_numbers(n, [2, 3, 5]))



'''
Recursion
'''
def factorial(i):
    if i == 0:   
        return 1
    else:
        return i * factorial(i - 1)
