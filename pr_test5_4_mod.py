# module for pr_test5.4.py
# file_search(folder, filename),

# -*- coding: utf-8 -*-

def file_search(path_list, name):
    res = path_list[0]
    print 'res=', res

    for i in path_list:
        print 'i|', i
        # check is_list
        if  i[0] == "[":
            print "Yaaaa"
        else:
            if i == name:
                res = res + '/' + name
                print 'yes', res
                break
            else:
                print 'no', res
                continue
'''        
            if res == 0:
                print 'the end false'
                return False
            else:
                print 'the another end'
                return res
    
'''
        
    
