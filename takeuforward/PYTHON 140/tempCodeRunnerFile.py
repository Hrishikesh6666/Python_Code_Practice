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