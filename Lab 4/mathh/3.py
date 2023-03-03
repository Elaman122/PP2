import math
a=int(input('Input number of sides: '))
b=int(input('Input the length of a side: '))
print('The area of the polygon is: ', int((pow(b , 2) *a) / (4 * math.tan((math.pi / a)))) ,sep = '')