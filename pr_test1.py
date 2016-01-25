import math
import sys
a = float(sys.argv[1])
b = int(sys.argv[2])
x = ((math.sqrt(a * b)) / ((math.e ** a) * b)) + a * math.e**((2 * a) /b)
print x
