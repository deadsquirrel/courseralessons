import re
def check_l(nnn):
    for line in nnn:
        if re.search('[a-zA-Z\._-]+@[a-z\.]+', line):
            print line
            p = re.compile('[a-zA-Z\._-]+@[a-z\.]+')
            n = p.findall(line)
            return n
    
