def Majority_element(arr):
    freq = {}
    
    for num in arr:
        freq[num] = freq.get(num,0)+1
        if freq[num] > len(arr)//2:
            return num
    return -1

# Example usage
arr = [2, 2, 1, 1, 1, 2, 2]
return_value = Majority_element(arr)
print(return_value)  # Output: 2




def Majority_element_another(arr):
    for i in range(len(arr)):
        if arr.count(arr[i]) > len(arr)//2:
            return arr[i]
    return -1
# Example usage
arr = [2, 2, 1, 1, 1, 2, 2]
return_value = Majority_element_another(arr)    
print(return_value)  # Output: 2