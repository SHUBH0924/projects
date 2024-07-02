# def find(arr):
#     min = arr[0]
#     for j in range(1, len(arr)):
#         if arr[j] < min:
#             min = arr[j]
#     return min

def find(arr):
    arr.sort()
    return arr[0]

arr = [10,30,22,133,-93]
print(find(arr))