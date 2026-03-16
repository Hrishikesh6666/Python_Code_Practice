##Remove Duplicates From an Unsorted Array
##Problem Statement: Given an unsorted array, remove duplicates from the array.


def remove_duplicates(arr):
    n = len(arr)
    result = []
    
    for i in range(n):
        duplicate = False
        
        for j in range(i):   # check only previous elements
            if arr[i] == arr[j]:
                duplicate = True
                break
        
        if not duplicate:
            result.append(arr[i])
            
    return result


arr = [1, 2, 2, 3, 4, 4, 5]
print("Array after removing duplicates:", remove_duplicates(arr))

## Maximum subarray sum , Kadanes Algorithm

def max_sum_subarray(arr):
    max_sum =0
    current_sum =0
    
    for i in range(1,len(arr)):
        current_sum = max(arr[i],current_sum + arr[i])
        max_sum = max(max_sum,current_sum)
    return max_sum

arr = [2,3,-8,7,-1,2,3]
print("Max sum of Subarray : ",max_sum_subarray(arr)) 

## The replacement by its rank in array

def rplace_rank(arr):
    sorted_arr = sorted(arr)
    
    rank = {}
    r = 1
    
    for num in sorted_arr:
        if num not in rank:
            rank[num] = r
            r += 1
    
    result = []
    for num in arr:
        result.append(rank[num])
        
    return result

arr = [1,1,5,5,3,3,4,4,4,8]
print(rplace_rank(arr))       

## Remove duplicates from the unsorted array

def remove_duplicates(arr):
    result =[]
    
    for i in range(len(arr)):
        found = False
        
        for j in range(len(result)):
            if arr[i] == result[j]:
                found = True
                break
            
        if not found:
            result.append(arr[i])
    return result

arr = [1,1,5,5,3,3,4,4,4,8]
print(remove_duplicates(arr))

   
## Max Sum Subarray of size K
'''
Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.
Note: A subarray is a contiguous part of any given array.
Examples:
Input: arr[] = [100, 200, 300, 400], k = 2
Output: 700
Explanation: arr2 + arr3 = 700, which is maximum.
'''

def max_sum_sliding(arr, k):

    n = len(arr)                                    # Size of array
    if n < k:                                       # Edge case: array smaller than k
        return -1

    # Step 1: Calculate sum of first window
    window_sum = sum(arr[:k])                       # Sum of first K elements
    max_sum = window_sum                            # Initialize max with first window

    # Step 2: Slide the window
    for i in range(k, n):                           # Start from kth index
        window_sum += arr[i]                        # Add new element (entering right)
        window_sum -= arr[i - k]                    # Remove old element (leaving left)
        max_sum = max(max_sum, window_sum)          # Update max sum if bigger

    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3
print(f"Max Sum (Sliding Window): {max_sum_sliding(arr, k)}")  # Output: 9


# Maximum Subarray sum , Kadanes algorithm

def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum= arr[0]
    
    for i in range(1,len(arr)):
        current_sum = max(arr[i],current_sum+arr[i])
        max_sum = max(max_sum,current_sum)
    return max_sum
arr = [2, 1, 5, 1, 3, 2]
print(max_subarray_sum(arr))

### count distinct element form in every window

def count_distinct_optimal(arr, k):
    n = len(arr)
    freq = {}
    result = []

    # first window
    for i in range(k):
        freq[arr[i]] = freq.get(arr[i], 0) + 1

    result.append(len(freq))

    # sliding window
    for i in range(k, n):
        incoming = arr[i]
        outgoing = arr[i-k]

        freq[incoming] = freq.get(incoming, 0) + 1

        freq[outgoing] -= 1
        if freq[outgoing] == 0:
            del freq[outgoing]

        result.append(len(freq))

    return result


arr = [1,2,1,3,4,2,3]
k = 4
print(count_distinct_optimal(arr,k))

