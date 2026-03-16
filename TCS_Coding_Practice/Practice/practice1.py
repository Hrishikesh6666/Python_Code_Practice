def first_non_repeating(s):
    freq={}
    
    for char in s:
        freq[char] =  freq.get(char,0)+1
        
    for char in s:
        if freq[char] == 1:
            return char   
    return -1
s ="aabbcde"
print(first_non_repeating(s))

#================== OR ============

def first_non_repeating(s):
    for i in range(len(s)):
        if s.count(s[i]) ==1:
            return s[i]
    return -1
print(first_non_repeating(s))

## Equilibrium index of an array

def equilibrium(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]
        
        if left_sum == right_sum:
            return i
        left_sum += arr[i]
    return -1
arr = [1, 3, 5, 2, 2]
print(equilibrium(arr))


## majority element 

def majority_element(arr):
    freq={}
    
    for num in arr:
        freq[num] = freq.get(num,0)+1
        if freq[num] > len(arr)//2:
            return num
    return -1
arr = [2,2,1,2,3,2,2]
print (majority_element(arr))

## matrix Transpose

def transpose_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    # Create an m x n result matrix filled with zeros
    result = [[0] * n for _ in range(m)]
    
    # Fill result with transposed values
    for i in range(n):
        for j in range(m):
            result[j][i] = matrix[i][j]
    
    return result   # return after finishing all loops

# Example
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(transpose_matrix(matrix))
