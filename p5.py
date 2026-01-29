while(1):
    n=input('enter any character (enter { to exit):')
    v=ord(n)
    if len(n)!=1:
           print('error,enter only 1 char')
    elif 48<=v<=57:
        print("value is a number or digit")
    elif 65<=v<=90:
        print("the value is an uppercase value")
    elif 97<=v<=122:
        print('the valis lowercase value')
    elif 33<=v<=47:
        print('special case')
    else :
        exit()