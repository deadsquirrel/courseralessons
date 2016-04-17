# module for pr_test5.4.py
# file_search(folder, filename),

# -*- coding: utf-8 -*-

def file_search(path_list, name):
    res = path_list[0]
    print 'res=', res

#>>> isinstance(a, list)
#True

    
    for i in path_list:
        print 'i|', i
        print type(i)
        # check is_list
        if i[0] == "[":
            print "Yaaaa"
        elif i[0] == "'":
            print "Ooooo"
        else: print "jjj"    
        '''
            if i == name:
                res = res + '/' + name
                print 'yes', res
                break
            else:
                print 'no', res
                continue
        '''
    
