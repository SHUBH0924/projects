def check(year):
    if year%4 == 0:
        print('leapyear')
    else:
        print('not leapyear')

if __name__ == '__main__':
    year = int(input('enter the year: '))
    check(year)