# find the smallest number in the array

arr = [1,3,4,2,5,6,7,8,1,4]

def smallest_element(arr):
    n = len(arr)
    min = arr[0]
    
    for i in range(n):
        if arr[i] < min:
            min = arr[i]
        return min
print(smallest_element(arr))


def largest_element(arr):
    max = arr[0]
    n = len(arr)
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
        return max
print(largest_element(arr))


def small_large_element(arr):
    arr.sort()
    small_element = arr[0]
    largest_element = arr[-1]
    return small_element , largest_element
print(small_large_element(arr))


##Second Smallest and Second Largest element in an array
arr = [1,3,4,2,5,6,7,8,1,4]
n = len(arr)
def secound_small(arr,n):
    small = float('inf')
    secound_small = float('inf')
    
    for i in range(n):
        if arr[i] < small:
            secound_small = small
            small = arr[i]
        elif arr[i] < secound_small and arr[i] != small:
            secound_small = arr[i]
    return secound_small

def secound_largest(arr,n):
    if n <2:
        return -1
    
    large = float('-inf')
    secound_large = float('-inf')
    
    for i in range(n):
        if arr[i] > large:
            secound_large = large
            large = arr[i] 
        elif arr[i] > secound_large and arr[i] != large:
            secound_large = arr[i] 
    return secound_large

print(secound_largest(arr,n),secound_small(arr,n))  
        
# reverse the array
arr = [1, 2, 3, 4, 5]
def reverse(arr):
    n = len(arr)
    reverse = arr[::-1]
    return reverse    

print(reverse(arr))

def reverse_arr(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        
        start += 1
        end -= 1
    return arr
print(reverse_arr(arr))

# count the frequency in the arr
arr = [10, 5, 10, 15, 10, 5]
def frequency_arr(arr):
    freq={}
    
    for num in arr:
        freq[num] = freq.get(num,0)+1
    return freq
print (frequency_arr(arr))

## Rearrange array in increasing-decreasing order

def increase_decreasing(arr):
    n = len(arr)
    
    mid = n//2
    
    for i in range(mid):
        print(arr[i],end=" ")
        
    for i in range(n-1,mid-1,-1):
        print(arr[i],end=" ")

arr = list(map(int,input("Enter:").split()))
increase_decreasing(arr)
    
# sum of element in the arr
arr = list(map(int,input("Enter:").split()))
def sum_elemnt(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

print(sum_elemnt(arr))

arr_sum = sum(arr)
print(arr_sum)
        
## Rotate array by K elements : Block Swap Algorithm 
def rotate_left(arr, d):
    n = len(arr)
    d = d % n
    if d == 0:
        return arr
    
    def reverse_section(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    # Step 1: Reverse first d elements
    reverse_section(0, d - 1)
    
    # Step 2: Reverse remaining n-d elements
    reverse_section(d, n - 1)
    
    # Step 3: Reverse entire array
    reverse_section(0, n - 1)
    
    return arr

# Example
arr = [10, 5, 10, 15, 10, 5]
d = 2
print(rotate_left(arr, d))

## average of element in the arr
arr = [10, 5, 10, 15, 10, 5]
def averge(arr):
    total = 0
    n = len(arr)
    for num in arr:
        total += num  
    avg = total / n
    return avg  
print(averge(arr))   
    
## Median of the given Array 
arr = [4, 7, 1, 2, 5, 6]
n = len(arr)
def midian_arr(arr,n):
    arr.sort()
    
    if n % 2 ==0:
        int1 = (n // 2) -1
        int2 = (n//2)
        print((arr[int1]+ arr[int2])/2)
    else:
        print(arr[n // 2])
         
print(midian_arr(arr,n))

## Remove Duplicates in-place from Sorted Array

def remove_duplicates(nums):
    if not nums:
        return 0
    
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    # Return both the new length and the modified array slice
    return i + 1, nums[:i+1]

# Example
arr = [1, 1, 2, 2, 3, 4, 4]
length, unique_arr = remove_duplicates(arr)
print("Length:", length)
print("Unique array:", unique_arr)

## Insert new element in the arr
def insert_element(arr, element, position):
    arr.insert(position-1, element)
    return arr


arr = list(map(int, input("Enter array elements: ").split()))
element = int(input("Enter element to insert: "))
position = int(input("Enter position: "))

print(insert_element(arr, element, position))

## Find Repeating Element in the arr
arr = [1, 1, 2, 3, 4, 4, 5, 2] 
def findRepeatingElement(arr):
    arr.sort()
    
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            print(arr[i],end=" ")
            
print(findRepeatingElement(arr))

# ========================OR ======================
from collections import Counter

# Function to find repeating elements in an array
def findRepeatingElements(arr):
    elementCount = Counter(arr)  # Count occurrences of each element
    
    print("The repeating elements are:", end=" ")
    # Print the elements that appear more than once
    for element, count in elementCount.items():
        if count > 1:
            print(element, end=" ")

# Driver code
arr = [1, 1, 2, 3, 4, 4, 5, 2]  # Example input
findRepeatingElements(arr)  # Call function to find repeating elements

## Find all the non-repeating elements in an array

from collections import Counter

def findNonRepeatingElement(arr):
    elementCount = Counter(arr)
    
    print("The nonrepeating element in the arr",end=" ")
    for element,count in elementCount.items():
        if count == 1:
            print(element,end =" ")
    
findNonRepeatingElement(arr)

#=========================OR=============

def findNonRepeatingElement(arr):
    hasmap={}
    
    for num in arr:
        hasmap[num] = hasmap.get(num,0)+1
        
    print("NonRepetaing number:",end=" ")
    
    for num,count in hasmap.items():
        # [if count > 1 ] for repeating element
        if count == 1:
            print(num,end=" ")
findNonRepeatingElement(arr)

## Find the all symmetrical pairs in the array

'''
Problem Statement: Given an array of pairs, find all the symmetric pairs in the array.
Example 1:
Input:
 (1,2),(2,1),(3,4),(4,5),(5,4)
Output:
 (2,1) (5,4)
Explanation:
 Since (1,2) and (2,1) are symmetric pairs and (4,5) and (5,4) are symmetric pairs.
'''

def find_symmetric_pairs(pairs):
    seen =set()
    
    for a,b in pairs:
        if (b,a) in seen:
            print("(",a,",",b,")",sep="",end=" ")
        else:
            seen.add((a,b))
pairs = [(1,2),(2,1),(3,4),(4,5),(5,4)]
find_symmetric_pairs(pairs)


## You are giving the square matrix A and B each of size N*N your task is to 
# compute the sum of their two metrics and store the result in the matrix A itself

def add_matrix(a,b):
    n = len(a)
    
    for i in range(n):
        for j in range(n):
            a[i][j] += b[i][j]
    return a
    
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
result = add_matrix(A, B)
print("Resultant Matrix:")
for row in result:
    print(row)

# Replace elements by its rank in the array
    
class Solution:
    # Function to replace elements by their rank in the array
    def replaceWithRank(self, arr):
        # Make a sorted copy of the array
        sorted_arr = sorted(arr)

        # Create a dictionary to hold ranks
        rank_map = {}

        # Initialize rank counter
        rank = 1

        # Assign ranks to unique elements
        for num in sorted_arr:
            if num not in rank_map:
                rank_map[num] = rank
                rank += 1

        # Build the result using rank map
        result = [rank_map[num] for num in arr]
        return result

# Driver code
obj = Solution()
arr = [1, 5, 8, 15, 8, 25, 9]
res = obj.replaceWithRank(arr)
print(*res)

##  maximum subarray sum IMP 

def max_subarray_sum(arr):

    max_sum     = arr[0]             # Step 1: Best sum seen so far (start with first element)
    current_sum = arr[0]             # Step 2: Current running sum (start with first element)

    for i in range(1, len(arr)):     # Step 3: Loop from 2nd element onwards
        current_sum = max(arr[i], current_sum + arr[i])  # Step 4: Extend or restart
        max_sum     = max(max_sum, current_sum)           # Step 5: Update best if needed

    return max_sum                   # Step 6: Return the best sum found


arr = list(map(int, input("Enter numbers separated by space: ").split()))
print("Maximum Subarray Sum:", max_subarray_sum(arr))

## Maximum SUM Subarray of size K


def max_sum_sliding(arr,k):
    n = len(arr)
    # Sum of the first 
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k,n):
        
        window_sum += arr[i] 
        window_sum  -= arr[i-k]
    
        max_sum = max(max_sum,window_sum)
    return max_sum

arr = list(map(int, input("Enter numbers separated by space: ").split()))
k = 3
print("Maximum Subarray Sum:", max_sum_sliding(arr,k))


