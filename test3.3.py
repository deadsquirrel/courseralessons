try:
    inp = raw_input ("Enter number: ")
    number = float (inp)
    print number
    if number <= 1.0:
        print "<=1.0"
        if number >=0.0:
            print ">=0.0"
            if number >= 0.9:
                print "A"
            elif number >= 0.8:
                print "B"
            elif number >= 0.7:
                print "C"
            elif number >= 0.6:
                print "D"
            else:
                print "F"
            
        else:
            print "enter another number"
    else:
        print "enter another number"
except:
    print "error!"
    
    
