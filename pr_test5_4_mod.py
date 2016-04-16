# module for pr_test5.4.py
# file_search(folder, filename),

def file_search(path, name):
    res = 0
    print 'res=', res

    for i in path:
        print 'i|', i
        if i == name:
            res = res + 'name'
            return res
        else:
            continue
        
        if res == 0:            
            return False
        else:
            return res
          
        print 'the end'

        
    
