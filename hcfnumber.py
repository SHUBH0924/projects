def gcd(num1,num2):
    while num1!=num2:
        if num1>num2:
            num1=num1-num2
        else:
            num2 -= num1
    print(num1)

num1 = int(input())
num2 = int(input())
gcd(num1,num2)