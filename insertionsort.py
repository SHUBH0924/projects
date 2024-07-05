def sort(arr):
    n=len(arr)
    for i in range(1,n+1):
        for j in range(0,n-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr = [10,30,22,133,-93]
print(sort(arr))