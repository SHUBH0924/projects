def sort(arr):
    """Sorts an array of integers in ascending order using the bubble sort algorithm."""
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
        
arr = [10,30,23,20,34,94]
print(sort(arr))