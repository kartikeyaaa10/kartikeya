a=int(input('enter height 1:'))
b=int(input('enter height 2:'))
c=int(input('enter height 3:'))

if a>b and a>c :
    print('person 1 is tallest')
elif b>a and b>c:
    print('person2 is tallest')
elif c>a and c>b:
    print('person 3 is tallest')
else:
    print('they are the same height')
    