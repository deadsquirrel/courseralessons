'''
examples for me
'''
#----------
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print(0)

#----------
#razobrat
>>>names = ['Amir', 'Bear', 'Charlton', 'Daman']                                                                      
>>>print names[-1][-1]

#----------
>>> list1 = [3, 4, 5, 20, 5, 25, 1, 3]
>>> list1.count(5)


#----------
my_tuple = (1, 2, 3, 4)
my_tuple.append( (5, 6, 7) )
print len(my_tuple)

#----------
>>> f = open('1.txt')
>>> ints = []
>>> try:
...     for line in f:
...         ints.append(int(line))
... except ValueError:
...     print('Это не число. Выходим.')
... except Exception:
...     print('Это что ещё такое?')
... else:
...     print('Всё хорошо.')
... finally:
...     f.close()
...     print('Я закрыл файл.')
...     # Именно в таком порядке: try, группа except, затем else, и только потом finally.
...
Это не число. Выходим.
Я закрыл файл.


#----------
def foo():
    return total + 1
total = 0
print(foo())

#----------


>>> class A:
...     def __init__(self, name):
...         self.name = name
...
>>> a = A('Vasya')
>>> print(a.name)
Vasya
