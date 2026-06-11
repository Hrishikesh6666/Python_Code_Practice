## Find the smallest number in an array

def smallest(arr):
    if len(arr) ==0:
        return None
    
    min =arr[0]
    for num in arr:
        if num < min:
            min = num
    return min
# Example usage
arr = [5, 2, 9, 1, 5, 6]
result = smallest(arr)
print("The smallest number in the array is:", result)

# find the largest number in the array

def largest(arr):
    if len(arr)==0:
        return None
    
    max = arr[0]
    
    for num in arr:
        if num > max:
            max = num
    return max
# Example usage
arr = [5, 2, 9, 1, 5, 6]
result = largest(arr)
print("The largest number in the array is:", result)

#  Brute force approach to find the smallest and largest numbers in an array

def find_smallest_largest(arr):
    sorted_arr = sorted(arr)
    return sorted_arr[0], sorted_arr[-1]
# Example usage
arr = [5, 2, 9, 1, 5, 6]
smallest_num, largest_num = find_smallest_largest(arr)
print("The smallest number in the array is:", smallest_num)
print("The largest number in the array is:", largest_num)

# Second largest and second smallest elements in the array

def second_smallesr(arr):
    min = second_min = float('inf')
    for num in arr:
        if num < min:
            secound_min = min
            min = num
        elif min < num < secound_min:
            secound_min = num
    return secound_min
def second_largest(arr):
    max =secound_max = float('-inf')
    for num in arr:
        if num > max:
            secound_max = max
            max = num
        elif max > num > secound_max:
            secound_max = num
    return secound_max
# Example usage
arr = [5, 2, 9, 1, 5, 6]
second_smallest_num = second_smallesr(arr)
second_largest_num = second_largest(arr)
print("The second smallest number in the array is:", second_smallest_num)
print("The second largest number in the array is:", second_largest_num)

## Reverse an array
arr = [5, 2, 9, 1, 5, 6]
reverse_arr = arr[::-1]
print("Reversed array:", reverse_arr)

left = 0
right = len(arr) -1
while left < right:
    arr[left],arr[right] = arr[right],arr[left]
    
    left += 1
    right -= 1
print("Reversed array:", arr)

# Find the frequency of each element in the array
def frequency(arr):
    freq ={}
    for num in arr:
        freq[num] = freq.get(num,0) +1
    return freq
# Example usage
arr = [5, 2, 2, 9,1,1, 1, 5, 6]
freq_result = frequency(arr)
print("Frequency of each element in the array:", freq_result)

## find the increasing and decreasing order of the array

def rearrangeArray(self, arr):
    # Sort the array
    arr.sort()

    n = len(arr)
        # Reverse the second half
    arr[n//2:] = reversed(arr[n//2:])

    return arr
# Example usage     
arr = [5, 2, 9, 1, 5, 6]
rearranged_arr = rearrangeArray(arr)    
print("Rearranged array in increasing and decreasing order:", rearranged_arr)


## Given an array arr rotate the array to the left by D steps where D is a positive
# integer Do it mandatory change in the array in the place

def rotateLeft(arr, d):
    n =len(arr)
    d = d % n
    
    def reverse(start, end):
        while start < end:
            arr[start],arr[end] = arr[end],arr[start]
            start += 1
            end -= 1
    
    reverse(0, d-1)
    reverse(d,n-1)
    reverse(0,n-1)
    return arr
# Example usage
arr = [1, 2, 3, 4, 5]
d = 2
rotated_arr = rotateLeft(arr, d)
print("Array after left rotation:", rotated_arr)


# sum of all the element in the array
def sum(arr):
    total =0
    for num in arr:
         total += num
    return total
print("Sum of all the elements in the array:", sum(arr))

## Average of all the elements in the array

total = sum(arr)
n = len(arr)
average = total / n
print("Average of all the elements in the array:", average)

## find the median of the array
def getMedian(arr, n):
    arr.sort()  # Sort the array to arrange elements in order
    
    if n % 2 == 0:
        # If the array size is even, calculate the average of two middle elements
        ind1 = (n // 2) - 1
        ind2 = (n // 2)
        print((arr[ind1] + arr[ind2]) / 2)  # Return the median for even-sized array
    else:
        # If the array size is odd, return the middle element
        print(arr[n // 2])
# Example usage
arr = [5, 2, 9, 1, 5, 6 ]
n = len(arr)
getMedian(arr, n)
