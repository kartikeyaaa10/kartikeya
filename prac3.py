sport=['cricket','football','khokho','basketball']

def display_task():
    for i in sport:
        print(i)
def add_task():
    sports=input('enter sports')
    sport.append(sports)
    display_task()

def remove_task():
    pos=int(input('enter the posn to be cancelled'))
    sport.pop(pos-1)
    display_task
def update_task():
    pos=int(input('enter posn to be updated '))
    sports=input('enter sports to be added ')
    sport.insert(pos-1,sports)
    display_task()
def sort_task():
    sport.sort()
    display_task()

def main():
    while(1):
        print('1.display 2.add 3.remove 4.update 5.sort 6.exit')
        ch=int(input('enter choice from 1 to 6'))

        if ch==1:
            display_task()
        elif ch==2:
            add_task()
        elif ch==3:
            remove_task()
        elif ch==4:
            update_task()
        elif ch==5:
            sort_task()
        elif ch==6:
            exit()
main()
