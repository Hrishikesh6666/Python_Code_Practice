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
    return i+1

# Example usage
arr = [1, 1, 2, 3, 3, 4,4,4,5,5,5]
new_length = remove_duplicates(arr)
print("Array after removing duplicates:", arr[:new_length])


## Array is sorted or not

def is_sorted(arr):
    n = len(arr)
    for i  in range(1,n):
        if arr[i] < arr[i-1]:
            return False
    return True

sorted_arr = is_sorted(arr)
if sorted_arr:
    print("The array is sorted.")
else:  
    print("The array is not sorted.")
    
    
## Max consecutive ones in a array

def max_consecutive_ones(arr):
    max_count =0 
    current_count =0
    
    for num in arr:
        if num ==1:
            current_count +=1
            max_count = max(max_count,current_count)
        else:
            current_count = 0
    return max_count

# Example usage

arr = [1, 1, 0, 1, 1, 1, 0, 1]
result = max_consecutive_ones(arr)  
print("Maximum number of consecutive ones:", result)


## Given two arrays a[] and b[] ,your task is to determine wether b[] is a subset of a[] or not

def is_subset(a, b):
    freq = {}
    
    # Count the frequency of elements in array a
    for num in a:
        freq[num] = freq.get(num,0)+1
        
    # Check if each element in array b is present in array a with sufficient frequency
    for num in b:
        if num not in freq or freq[num] == 0:
            return False
        freq[num] -= 1
    return True
# Example usage
a = [1, 2, 3, 4, 5] 
b = [2, 3, 4]
result = is_subset(a, b)
if result:
    print("b[] is a subset of a[].")    
else:    print("b[] is not a subset of a[].")   




## Given an array arr rotate the array to the left by D steps where D is a positive
# integer Do it mandatory change in the array in the place

def rotate_left(arr, d):
    n = len(arr)
    d = d%n  # Handle cases where d is greater than n
    
    def reverse(start,end):
        while start < end :
            arr[start], arr[end] = arr[end] , arr[start]
            start += 1
            end -= 1
            
    # Reverse the first d elements
    reverse(0 , d-1)
    # Reverse the remaining elements
    reverse(d , n-1)
    # Reverse the entire array
    reverse(0 , n-1)
    
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
d = 2
result = rotate_left(arr, d)
print("Array after left rotation:", result)


##  This is again the Equilibrium Index problem, but phrased as: 
# Optimal Approach (Running Sum)
# 💡 Core Idea: 
# Compute total sum.
# Maintain running left sum.
# Right sum = total_sum - left_sum - arr[i].

def equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]
        
        if left_sum == right_sum:
            return i  # Return the equilibrium index
        
        left_sum += arr[i]
    return -1  # No equilibrium index found
# Example usage
arr = [-7, 1, 5, 2, -4, 3, 0]
result = equilibrium_index(arr) 
if result != -1:
    print("Equilibrium index found at:", result)
else:    print("No equilibrium index found.") 


## Adding the two matrices

def add_matrices(a,b):
    
    n = len(a)
    
    for i in range(n):
        for j in range(n):
            a[i][j] += b[i][j]
    return a
# Example usage
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = add_matrices(a, b)
print("Result of adding the two matrices:")
for row in result:
    print(row)
