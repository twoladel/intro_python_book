value = int(input('Enter a number: '))

match value:
    case 1 | 2 | 3:
        print('value is < than 4')
    case 4 | 6 | 8:
        print('value is divisible by 2, but not equal to 2')
    case 5:
        print('value is 5')
    case 7:
        print('value is 7')
    case _: #default case
        print('value is not 1 thru 8')