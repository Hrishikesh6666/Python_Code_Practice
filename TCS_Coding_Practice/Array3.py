## Smallest element in an array
def smallest_element(arr):
    if not arr:
        raise ValueError("Array cannot be empty")
    
    smallest = arr[0]
    for num in arr:
        if num<smallest:
            smallest = num
    return smallest
    
# Example usage
arr=[5, 2, 9, 1, 5, 6]
print("Smallest element:", smallest_element(arr))

# OR ANOTHER WAY BRUTE FORCE

def smallest_element(arr):
    sorted_arr = sorted(arr)
    return sorted_arr[0],sorted_arr[-1]
print("Smallest and Largest elements:", smallest_element(arr))

## Largest element in the array
def largest_element(arr):
    if not arr:
        raise ValueError("Array cannot be empty")
    
    largest_element= arr[0]
    for num in arr:
        if num>largest_element:
            largest_element = num
    return largest_element

# Example usage
print("Largest element:", largest_element(arr))


## secound largest and secound smallest element in the array

# Approach 1: Using sorting BROTE FORCE
def second_largest_smallest(arr):
    unique = list(set(arr))
    
    if len(unique) < 2:
        raise ValueError("Array must have at least two unique elements")
    
    sorted_arr = sorted(unique)
    return sorted_arr[1], sorted_arr[-2]
print("Second smallest and second largest elements:", second_largest_smallest(arr))

# Approach 2: Using single pass
def second_largest_smallest(arr):
    if len(arr) < 2:
        raise ValueError("Array must have at least two elements")
    
    smallest = min(arr)
    largest = max(arr)
    
    second_smallest = float('inf')
    second_largest = float('-inf')
    
    for num in arr:
        if smallest < num < second_smallest:
            second_smallest = num
        if largest > num > second_largest:
            second_largest = num
    if second_smallest == float('inf') or second_largest == float('-inf'):
        raise ValueError("Array must have at least two unique elements")
    return second_smallest, second_largest
print("Second smallest and second largest elements:", second_largest_smallest(arr))


## REVERSE OF AN ARRAY

def reverse_array(arr):
    # arr.sort() # Sort the array in ascending order
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left],arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
# Example usage 
print("Reversed array:", reverse_array(arr))

reverse_array = arr[::-1]
print("Reversed array:", reverse_array) 


## Count frequency of each element in the array

def count_frequency(arr):
    freq={}
    
    for num in arr:
        freq[num] = freq.get(num,0)+1
    return freq
# Example usage
arr = [1, 2, 2, 3, 3, 3, 4]
frequency = count_frequency(arr)
print("Frequency of each element:", frequency)

# another way using collections module

def count_frequency(arr):
    if not arr:
        return
    
    arr.sort()
    count = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            count += 1
        else:
            print(arr[i-1],count)
            count = 1
    print(arr[-1], count)
# Example usage
print("Frequency of each element:") 
count_frequency(arr)


## rearrange the array in increasing-decreasing order You need ordering + controlled placement

# arr=[8,7,1,6,9,5] -> [1,5,6,7,9,8] 


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

# =========OR ANOTHER WAY ============

def rearrange_array(arr):
    n =len(arr)
    arr.sort()
    
    mid = n//2
    result =[]
    
    # first half in increasing order
    for i in range(mid):
        result.append(arr[i])
    # second half in decreasing order
    for i in range(n-1, mid-1,-1):
        result.append(arr[i])
    return result
# Example usage
print ("Rearranged array:", rearrange_array(arr))


## Sum of all elements in the array
def sum_of_elements(arr):
    total = 0
    for num in arr:
        total += num
    return total
# Example usage
arr = [1, 2, 3, 4, 5]
print("Sum of all elements:", sum_of_elements(arr))



result = sum(arr)
print("Sum of all elements:", result)


## Sum of first n natural numbers
n =10
total = 0
for i in range(1,11):
    total += n*i
print("Sum of first 10 natural numbers:", total)


## ======================================================
# Rotate array by K elements : Block Swap Algorithm
# Problem Statement: Given an array of n size, rotate the array by k elements using the Block Swap Algorithm.
# Examples
# Input : N = 5, array[] = {1, 2, 3, 4, 5}, K = 2
# Output (Left Rotation) : {3, 4, 5, 1, 2}
# Explanation : After rotating left by 2, the first two elements move to the end.


def rotate_left(arr,d):
    n=len(arr)
    d = d%n # Handle cases where d is greater than n
    
    def reverse(start,end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
            
    # Step 1: Reverse the first d elements
    reverse(0,d-1)
    # Step 2: Reverse the remaining n-d elements
    reverse(d,n-1)
    # Step 3: Reverse the entire array
    reverse(0,n-1)
    
    return arr
# Example usage
arr = [1,8,9,12,45,64,23]
d =3
print("Array after left rotation:", rotate_left(arr,d))


## Average of all the elements in the array

def avg(arr):
    total = sum(arr)
    n = len(arr)
    if n == 0:
        raise ValueError("Array cannot be empty")
    return total/n
# Example usage
arr = [1, 2, 3, 4, 5]
print("Average of all elements:", avg(arr))

## find the median of the array

def median(arr):
    n=len(arr)
    arr.sort()
    if n == 0:
        raise ValueError("Array cannot be empty")
    
    if n%2 == 1:
        return arr[n//2]
    else:
        return (arr[n//2 -1] + arr[n//2])/2
# Example usage
arr = [1, 2, 3, 4, 5, 6]
print("Median of the array:", median(arr))

## Remove duplicates from the array

def remove_duplicates(arr):
    unique = list(set(arr))
    return unique
# Example usage
arr = [1, 2, 2, 3, 4, 4, 5]
print("Array after removing duplicates:", remove_duplicates(arr))

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
    
    
    