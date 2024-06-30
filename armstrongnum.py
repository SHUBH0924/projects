n = int(input("Enter the number\n"))
temp = n
sum = 0

while temp!=0:
    order = len(str(n))
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if sum == n :
    print("The number is an Armstrong number " + str(n))
else:
    print("The number is not an Armstrong number " + str(n))