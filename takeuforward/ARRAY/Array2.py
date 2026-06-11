arr = [1, 1, 2, 3, 3, 4]

def remove_duplicates(arr):
    if not arr:
        return 0
    
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i + 1

new_length = remove_duplicates(arr)
print("New length of the array after removing duplicates:", new_length)
print("Array after removing duplicates:", arr[:new_length])

# remove duplicates from unsorted array
def remove_duplicates_unsorted(arr):
    freq={}
    if not arr:
        return 0
    
    for num in arr:
        freq[num]=freq.get(num,0)+1
        
    i = 0
    for num in freq:
        if freq[num] == 1:
            arr[i] = num
            i += 1
    return i

# add elements to the array

def add_elements(arr, elements):
    arr.extend(elements)
    return arr

arr = [1, 2, 3]
new_elements = [4, 5, 6]
updated_arr = add_elements(arr, new_elements)
print("Array after adding elements:", updated_arr)

## Find all repeating elements in an array

def find_repeating_elements(arr):
    freq={}
    repeats=[]
    
    for num in arr:
        freq[num] = freq.get(num,0)+1
    
    for num,count in freq.items():
        if count > 1:
            repeats.append(num)
    return repeats

# Example usage
arr1 = [1, 1, 2, 3, 4, 4, 5, 2]
print("Repeating elements:", find_repeating_elements(arr1))  # Output: [1, 2, 4]

# find all non-repeating elements in an array

def find_non_repeating_elements(arr):
    freq={}
    non_repeats=[]
    
    for num in arr:
        freq[num]= freq.get(num,0)+1
    
    for num,count in freq.items():
        if count == 1:
            non_repeats.append(num)
    return non_repeats
# Example usage
arr1 = [1, 1, 2, 3, 4, 4, 5, 2]
print("Non-repeating elements:", find_non_repeating_elements(arr1))  # Output: [3, 5]



## Find all Symmetric Pairs in the array of pairs
# Example 1:
# Input:
#  (1,2),(2,1),(3,4),(4,5),(5,4)
# Output:
#  (2,1) (5,4)
# Explanation:
#  Since (1,2) and (2,1) are symmetric pairs and (4,5) and (5,4) are symmetric pairs.

def find_symmetric_pairs(pairs):
    seen={}
    result=[]
    for a,b in pairs:
        if seen.get(b) == a:
            result.append((a,b))
        else:
            seen[a] = b
    return result
# Example usage
pairs = [(1,2),(2,1),(3,4),(4,5),(5,4)]
print("Symmetric pairs:", find_symmetric_pairs(pairs))  # Output: [(2


# Sort Elements of an Array by Frequency

from collections import Counter

def sort_by_freq(arr):
    
    freq = Counter(arr)
    # for num in arr:
    #     freq[num] = freq.get(num, 0) + 1
    
    sorted_arr = sorted(arr , key=lambda x: (-freq[x], x))
    return sorted_arr
# Example 1
arr1 = [1, 1, 2, 3, 2, 4, 4, 4]
print("Sorted by frequency:", sort_by_freq(arr1))



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
            return i
        
        left_sum += arr[i]
    return -1

arr = [-7, 1, 5, 2, -4, 3, 0]
result = equilibrium_index(arr) 
if result != -1:
    print("Equilibrium index found at:", result)
else:    print("No equilibrium index found.") 

## Search an Element in an Array Using Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid + 1   # 1-based index
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage
arr = list(map(int, input("Enter sorted array elements: ").split()))
k = int(input("Enter target element: "))

pos = binary_search(arr, k)
if pos != -1:
    print("Element found at position:", pos)
else:
    print("Element not found")

##Check if array is subset of another array
#Problem Statement: Given arr1[] and arr2[], we need to find whether arr1[] is a subset of arr2[]. An array is called a subset of another if all of its elements are present in the other array..

def is_subset(arr1, arr2):
    set2 = set(arr2)
    for num in arr1:
        if num not in set2:
            return False
    return True

arr1 = list(map(int, input("Enter first array elements: ").split()))
arr2 = list(map(int, input("Enter second array elements: ").split()))

if is_subset(arr1, arr2):
    print("Array 1 is a subset of Array 2")
else:
    print("Array 1 is not a subset of Array 2")
