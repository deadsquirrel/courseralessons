import re

hand = open ('mbox-short.txt')
for line in hand:
    line-line.rstrip()
#   line.startswith ('From:'):    
    line re.search('^From:', line):
    print line

    
#some variants of program cut host from line

# Example 1
atpos = data.find('@')
print atpos

sppos = data.find(" ", atpos)
print sppos

host = data[atpos+1 ; sppos]
print host
# Output
# uct.ac.za


# Example 2
words = line.split()
email = words[1]
pieses = email.split('@')
print pieses [1]
# Output
# uct.ac.za


# Example 3
#import re
lin1 = 'From stephen.mardghkg@uct.ac.za fghhm,m11:03 fghgk'
y1 = re.findall('@([^ ]*)', lin1)
print y1
# Output
# ['uct.ac.za']

# Example 4
#import re
lin2 = 'From stephen.mardghkg@uct.ac.za Sat Jan 18:50'
y2 = re.findall('^From .*@([^ ]*)', lin2)
print y2
# Output
# ['uct.ac.za']

