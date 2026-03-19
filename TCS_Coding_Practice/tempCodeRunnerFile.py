# Remove duplicate elements from a sorted array
def remove_duplicates(arr):
    if not arr:
        return 0
    n= len(arr)
    i= 0
    for j in range(1,n):
        if arr[j] !=arr[i]:
            i+=1
            arr[i] =arr[j]
    return i

# Example usage
arr = [1, 1, 2, 3, 3, 4,4,4,5,5,5]
new_length = remove_duplicates(arr)
print("Array after removing duplicates:", arr[:new_length])