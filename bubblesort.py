def sort(arr):
    """Sorts an array of integers in ascending order using the bubble sort algorithm."""
    n=len(arr)
    for i in range(1,n):
        for j in range(0,n-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
        
arr = [10,30,23,20,34,94]
print(sort(arr))