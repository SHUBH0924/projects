def reverse(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num = num // 10
    return rev

num = int(input("enter number: "))
print("reverse of number is: ", reverse(num))