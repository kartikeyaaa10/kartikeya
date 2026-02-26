#define a grade calc which diplays grade of student if the precent is more than 90 g is O 
#if the percent is betwn 70 to 90 g is a , if the percent is betnwen 6- to 70 g is b, if the percent is betwn 40 to 60 grade is c under 40 is f
name = str(input('Enter your name : '))
am = int(input('Enter a marks in Maths : '))
ph = int(input('Enter a marks in Physics : '))
ch = int(input('Enter a marks in Chemistry : '))
ds = int(input('Enter a marks in Data Strcuture : '))
py = int(input('Enter a marks in Python : '))
eg = int(input('Enter a marks in Graphics : '))

grade = (am+ph+ch+ds+py+eg)/5
print(f'The grade of {name} is {grade} %',)

if grade >= 90 :
    print('O')
elif grade >=70 and grade<90 :
    print('A')
elif grade >=60 and grade<70 :
    print('B')
elif grade >=40 and grade<60 :
    print('C')
elif grade < 40:
    print('F')
else :
    print('Error!!')

