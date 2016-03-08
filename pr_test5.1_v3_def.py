def counter (a, b):
    list_a = []
    for item in set(a).difference(b):
        print item
        list_a.append(item)
        print a
        print b
    print "!",list_a
    return list_a
