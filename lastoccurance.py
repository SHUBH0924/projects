def findValueIndex(arr, i, val):
	if i == -1:
    	    return -1  # Return -1 to indicate that the value was not found in the array

	if arr[i] == val:
    	    return i  # Return the index if the value is found at this position
	return findValueIndex(arr, i -1, val)

# Example usage
arr = [1, 2, 3, 4, 5]
size = len(arr)
val = int(input("Enter the value to find: "))

index = findValueIndex(arr, size-1, val)

if index != -1:
	print(f"The value {val} is found at index {index}.")
else:
	print(f"The value {val} is not in the array.")


