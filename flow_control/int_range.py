def int_range(int):
    if int >= 0 and int <= 50:
        print(f'{int} is between 0 and 50')
    elif int >= 51 and int <= 100:
        print(f'{int} is between 51 and 100')
    elif int > 100:
        print(f'{int} is greater than 100')
    else:
        print(f'{int} is less than 0')

''' book solution was smarter, start with less than 0 and work your way up.
don't need to use any 'and' operators that way. '''

int_range(0)
int_range(25)
int_range(50)
int_range(75)
int_range(100)
int_range(101)
int_range(-1)
int_range(-35)