# two sum sorted input Given a sorted array and the target summer
# find two numbers such that they add up to the target return their indices or value


def two_sum_sorted(arr, target):
    start=0
    end=len(arr)-1
    
    while start<end:
        current_sum = arr[start]+arr[end]
        
        if current_sum == target:
            return [start, end]  # Return indices
        
        elif current_sum < target:
            start +=1
            
        else:
            end -=1
    return -1
# Example usage
arr = [1, 2, 3, 4, 5]           
target = 7
return_value = two_sum_sorted(arr, target)
print(return_value)  # Output: [1, 3] (since arr[1] + arr[3] = 2 + 5 = 7)



import bisect
def two_sum_sorted_builtin(arr, target):
    for i in range(len(arr)):
        complement = target - arr[i]
        j = bisect.bisect_left(arr, complement, i + 1)
        
        if j < len(arr) and arr[j] == complement:
            return [i, j]  # Return indices
    return -1

return_value = two_sum_sorted_builtin(arr, target)
print(return_value)  # Output: [1, 3] (since arr[1] + arr[3] = 2 + 5 = 7)