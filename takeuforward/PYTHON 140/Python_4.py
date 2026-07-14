## Write a Python Program to find largest element in an array.

arr = [int(x) for x in input("Enter the elements of the array separated by space: ").split()]

def largest_element(arr):
    if not arr:
        return None
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest
print("The largest element in the array is:", largest_element(arr))

## Write a Python Program to find smallest element in an array.

def smallest_element(arr):
    if not arr:
        return None
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest
print("The smallest element in the array is:", smallest_element(arr))

## Python Program for cube sum of first n natural numbers.
def cube_sum(n):
    if n <= 0:
        return 0
    return sum(i**3 for i in range(1,n+1))

n = int(input("Enter the value of n: "))
print("The cube sum of first", n, "natural numbers is:", cube_sum(n))

## Write a Python Program for array rotation.
arr = [int(x) for x in input("Enter the elements of the array separated by space: ").split()]
k = int(input("Enter the number of rotations: "))

def rotate_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

k %= len(arr)

rotate_array(arr, 0, k - 1)
rotate_array(arr, k, len(arr) - 1)
rotate_array(arr, 0, len(arr) - 1)

print(arr)       

arr = arr[k:] + arr[:k]

print("The array after rotation is:", arr)        
        
    
    