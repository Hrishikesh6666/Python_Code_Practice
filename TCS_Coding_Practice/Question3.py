def search_range(arr, target):
    
    def find_first():
        start, end = 0, len(arr) - 1
        first = -1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if arr[mid] == target:
                first = mid
                end = mid - 1  # <-- FIXED: Keep searching to the left
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return first
    
    def find_last():
        start, end = 0, len(arr) - 1
        last = -1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if arr[mid] == target:
                last = mid
                start = mid + 1 # Keep searching to the right
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return last
    
    return [find_first(), find_last()]

arr = [5, 7, 7, 7, 7, 8, 8, 8, 10]
target = 8
print(search_range(arr, target)) # Output: [3, 5]


# ==================================================================
# Another way to find the first and last position of an element in a sorted array
# Using built-in functions
#===================================================================

import bisect
def search_range_builtin(arr,target):
    if not arr:
        return [-1,-1]
    left = bisect.bisect_left(arr,target)
    if left == len(arr) or arr[left] != target:
        return [-1,-1]
    
    right = bisect.bisect_right(arr,target)-1
    return [left,right]
target = 7
print(search_range_builtin(arr,target))