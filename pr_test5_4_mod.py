# module for pr_test5.4.py
# file_search(folder, filename),

def file_search(path_list, name):
    res = path_list[0]
    print 'res=', res

    for i in path_list:
        print 'i|', i
        if i == name:
            res = res + '/' + name
            print 'yes', res
            break
        else:
            print 'no', res
            continue
        
    if res == 0:
        print 'the end false'
        return False
    else:
        print 'the another end'
        return res
    

        
    
