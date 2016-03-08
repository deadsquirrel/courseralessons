def counter (a, b):
    list_a = []
    for item in set(b).difference(a):
#        print item
        list_a.append(item)
#        print a
#        print b
#    print "!",list_a
#    for i in set(b).difference(list_a)
    return list_a
