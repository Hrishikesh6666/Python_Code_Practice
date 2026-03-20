def rearrange_array(arr):
    n = len(arr)
    arr.sort()
    
    mid = n//2
    left = mid
    right = n-1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
# Example usage
arr=[8,7,1,6,9,5]
print("Rearranged array:", rearrange_array(arr))