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
            for y in i:
                print "y==", y
                if y == name:
                    pr_test5_4_mod.file_search2(i[1:-1], name)
                else: break
        else: print "jjj"

def file_search2 (p, name):
    print "-----"
    for j in p:
        if j == name:
            res = res + '/' + name
            print 'yes', res
            break
        else:
            print 'no', res
            continue

    
