# Some of starting 10 multiple of a given numbers

n =10
total = 0
for i in range(1,11):
    total += n * i
    print(total)
    
# Sum of element in an array    

arr = [1,2,3,4,5]
total = sum(arr)
print(total)

## or
total = 0
for num in arr:
    total += num
print("Sum of elements in the array:", total)

## Mean of the array

mean  = sum(arr)/ len(arr)
print("Mean of the array:", mean)

## largest element in the array
Arr = [22, 45, 67, 89, 12 ,34]
sorted_arr = sorted(Arr)
largest_element = sorted_arr[-1]
smallest_element = sorted_arr[0]
print("Largest element in the array:", largest_element)
print("Smallest element in the array:", smallest_element)

#or

max = Arr[0]

for num in Arr:
    if num > max:
        max = num
print("Largest element in the array:", max)

## Smallest element in the array

min = Arr[0]

for num in Arr:
    if num < min:
        min = num
print("Smallest element in the array:", min)


## Reverse of an array

reversed_arr =Arr[::-1]
print("Reversed array:", reversed_arr)

#or 

left = 0
right = len(Arr)-1
while left<right:
    Arr[left], Arr[right]= Arr[right], Arr[left]
    left += 1
    right -= 1 
print("Reversed array:", Arr)

def matrix_Trenspose(matrix):
    n =len(matrix)
    m =len(matrix[0])
    result = [[0]*n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            result[j][i] = matrix[i][j]
    return result
matrix = [[1, 2, 3],
          [4, 5, 6],        
          [7, 8, 9]]
transposed_matrix = matrix_Trenspose(matrix)
print("Transposed matrix:", transposed_matrix)

# Secound largest element in the array

sorted_arr = sorted(Arr)
second_largest = sorted_arr[-2]
print("Second largest element in the array:", second_largest)

#or 

if len(Arr) < 2:
    print("Array does not have enough elements to find the second largest.")
else:
    max = second_max = float('-inf')
    for num in Arr:
        if num > max:
            second_max = max
            max = num
        elif second_max < num < max:
            second_max = num
    if second_max == float('-inf'):
        print("There is no second largest element in the array.")
    else:
        print("Second largest element in the array:", second_max)