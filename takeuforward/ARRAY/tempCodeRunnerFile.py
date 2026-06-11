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