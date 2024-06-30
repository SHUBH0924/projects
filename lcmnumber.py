# def lcm(num1,num2):
#     maximum = num1 if num1>num2 else num2
#     limit = num1*num2
#     for i in range(maximum,limit+1,maximum):
#         if i%num1==0 and i%num2==0:
#             print (i)
#             break

# def lcm(num1,num2):
#     temp1 = num1 
#     temp2 = num2
#     while temp1!=temp2:
#         if temp1>temp2:
#             temp1=temp1-temp2
#         else:
#             temp2=temp2-temp1
#     # return temp1
#     lcm =  num1*num2/temp1
#     print(int(lcm))

def lcm(num1,num2):
    m = num1 if num1>num2 else num2
    temp = m
    while True:
        if m%num1==0 and m%num2==0:
            print(m)
            break
        m+=temp

num1 = int(input())
num2 = int(input())
lcm(num1,num2)