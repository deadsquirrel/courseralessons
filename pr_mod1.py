'''
Decrypt message
Bacon's cipher
'''
import sys
inp = sys.argv[1]
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
n = 0
k = 5
key_v = []
newl = []

'''
create list of tuple with key_value_structure = key_letter_of_alphabet
'''
for i in alphabet:
    y = (i, key[n:k])
#    print "n:",n,"y:", y
    key_v.append(y)
    n = n + 1
    k = k + 1

#print key_v

'''
a.islower() .
a.isupper(), b.isupper(), c.isupper(), d.isupper()
True False
 "a" or "b"
'''
print inp
for j in inp:
    if j == " ":
#        newl.append(j)
        continue
    else:
        low = j.islower()
        if low == True:
            newl.append('a')
        else:
            newl.append('b')

print "------------"      
print newl
print "------------"      

counter = len(newl)
while counter > 0:
    print "N",counter 
    word = newl[0:5]
    print "word:",word
    newnl = newl.replace(word, "")
    print "shortline::",newnl
    counter = counter - 5
