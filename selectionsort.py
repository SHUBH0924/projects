def selection_sort(arr,n):
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr

arr = [98,32,12,87,31,399,47]
n=len(arr)
print(selection_sort(arr,n))