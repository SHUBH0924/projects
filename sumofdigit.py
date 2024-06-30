def sumofdigit(num):
    s = 0
    while num != 0:
        s += num % 10
        num //= 10
    print(s)

num = int(input("Enter the number: "))
sumofdigit(num)