def remove_duplicates(arr):
    if not arr:
        return 0
    n = len(arr)
    i = 0
    for j in range (1,n):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return arr[:i+1]
# Example usage
arr = [1, 2, 2, 3, 4, 4, 5]
print("Array after removing duplicates:", remove_duplicates(arr))
    