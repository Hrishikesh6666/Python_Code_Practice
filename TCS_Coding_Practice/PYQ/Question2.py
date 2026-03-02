# Given an array of 0s and 1s,
# find the longest subarray where:
# number of 0s == number of 1s
# Return the length.
# Example
# Input: [0,1,0,1,1,1,0]
# Output: 4
# One longest balanced subarray:
# [0,1,0,1]


def longest_balanced_subarray(arr):
    diff = 0
    max_length = 0
    first_occurrence = {0: -1}  # To handle the case when the balanced subarray starts from index 0
    
    zeros = 0
    ones = 0 
    
    for i in range(len(arr)):
        if arr[i] == 0:
            zeros += 1
        else:
            ones += 1
            
        diff = zeros - ones
        if diff in first_occurrence:
            length = i - first_occurrence[diff]
            max_length = max(max_length, length)
        else:
            first_occurrence[diff] = i
    return max_length

# Example usage:
input_array = [0, 1, 0, 1, 1, 1, 0]
result = longest_balanced_subarray(input_array)
print(result)  # Output: 4