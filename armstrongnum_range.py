start = int(input('enter the start'))
end = int(input('enter the end'))

for num in range(start, end+1):
    sum = 0
    temp = num
    while temp > 0:
        order = len(str(num))
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num)