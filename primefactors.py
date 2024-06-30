import math
def primefactor(num):
    for i in range(2, math.ceil(math.sqrt(num)+1)):
        while num%i==0:
            print(i)
            num=num/i
    if num>2:
        print(int(num)) 


num = int(input())
primefactor(num)