import math

def is_prime(n):
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
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

