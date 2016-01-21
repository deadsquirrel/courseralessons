largest = None
smallest = None

while True:
    try:
        inp = raw_input("Enter a number: ")
        if inp == "done" : 
            break
        else:
            num = int (inp)
            if largest is None:
                largest = num
                smallest = num
                print  "largest", largest, "smallest", smallest
            elif num > largest:
                largest = num
                print "largest", largest
            elif num < smallest:
                smallest = num
                print "smallest", smallest
            else:
                print "other"
                print "largest", largest, "smallest", smallest, "num", num
                print 
    except:
        print "Invalid input"    
        
print "Maximum is", largest
print "Minimum is", smallest
