def check(num):
    rev = 0
    temp = num
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10
    if rev == num:
        print("is_palindrome")
    else:
        print("is_not_palindrome")

num = int(input("enter number: "))
check(num)