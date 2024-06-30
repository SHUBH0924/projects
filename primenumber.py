import math
def prime(num):
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count += 1
    if count > 2 :
        print(f"{num} not prime")
    else:
        print(f"{num} is prime")

num = int(input("Enter the number\n"))
prime(num)

'''
isprime = True
n = 5

if n < 2:
    isprime = False
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            isprime = False
            break

if isprime:
    print("Number is a Prime Number")
else:
    print("Number is not a Prime Number")

Algorithm 2
from math import sqrt

def isprime(n):
    # 0 and 1 are not prime numbers
    # negative numbers are not prime
    if n <= 1:
        return False
    # special case as 2 is the only even number that is prime
    elif n == 2:
        return True
    # Check if n is a multiple of 2, thus all these won't be prime
    elif n % 2 == 0:
        return False
    # If not, then just check the odds
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
'''