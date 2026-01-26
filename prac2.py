import math

print('1.circle')
print('2.rectangle')
print('3.triangle')
ch=int(input('enter choice'))
if ch==1:
    r=int(input('enter radius'))
    print('area of circle is=',math.pi*r*r)
if ch==2:
    l=int(input('enter length '))
    b=int(input('enter breadth '))
    print('area of rectangle is ',l*b)
if ch==3:
    ba=int(input('enter base'))
    h=int(input('enter height'))
    print('area of triangle:',0.5*ba*h)
