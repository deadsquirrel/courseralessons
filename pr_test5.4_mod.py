# module for pr_test5.4.py
# file_search(folder, filename),

def file_search(path, name)
res = path[0]
print res

for i in path:
    if i == name:
        res = res + 'name'
        return res
    else:
        print False
        return False


print 'the end'

        
    
