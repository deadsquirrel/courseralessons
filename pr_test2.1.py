import math
import sys

x = float(sys.argv[1])
m = float(sys.argv[2])
s = float(sys.argv[3])
#dd = 2.0

#y = math.exp(-1.0*(math.pow(x - m, dd) / (dd * math.pow(s, dd))))
#print y
#z = s * math.sqrt(dd * math.pi)
#print z
#f = (1 / z )* y



f = 1 /(s * math.sqrt(2 * math.pi)) * math.exp(-1*(x - m) ** 2 / (2 * s ** 2))
print f
