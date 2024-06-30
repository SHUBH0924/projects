def linear_search(arr,item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return 'not found'

arr = [10,30,22,133,-93]
item = -9
print(linear_search(arr,item))