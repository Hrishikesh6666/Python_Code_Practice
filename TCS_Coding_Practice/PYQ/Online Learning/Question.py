
# The Logic
# To solve this, we need to track how many times each element appears in the array. The most efficient way to do this is by using a
# Hash Map (a Dictionary in Python).
# We will iterate through the array one by one.
# As we encounter each number, we store it in our dictionary and keep a running tally of its occurrences.
# Once the entire array is processed, we iterate through our dictionary.
# If an element's total count is cleanly divisible by 2 (i.e., count % 2 == 0), it has appeared an even number of times, and we print it.

n = int(input("Enter the number:").strip())

arr = list(map(int, input("Enter the array elements: ").split()))
if len(arr) != n :
    print("Invalid input")
else:
    freq = {}
    # count the frequency of each element in the array
    for num in arr:
        freq[num] = freq.get(num,0)+1
    #print the element with even frequency
    
    result = [key for key, value in freq.items() if value % 2 == 0]
    if result:
        print(*result)
    else:
        print("No even frequency elements found")
    
##============================ OR ==========================
def even_frequency(arr):
    freq = {}
    
    for num in arr:   # iterate over elements, not range(n)
        freq[num] = freq.get(num, 0) + 1
        # another methode to calculate frequency 
        # if arr[num] in freq : freq [arr[num]] +=1
    
    for key in freq:
        if freq[key] % 2 == 0:
            print(key)

arr = [1,2,3,4,5,6,7,8,9,2,4,6,8]  # example input
even_frequency(arr)

#================================another way ==================
n = int(input("Enter size: "))
arr = list(map(int, input("Enter: ").split()))

for i in range(n):
    count = 0
    
    for j in range(n):
        if arr[i] == arr[j]:
            count += 1
    
    # check AFTER finishing the count
    if count % 2 == 0:
        if arr[i] not in arr[:i]:   # ensures no duplicates printed
            print(arr[i])

## ====================TCS -Format =========================

from collections import Counter
n = int(input("Enter size: "))
arr = list(map(int, input("Enter: ").split()))

def find_even_freq(n,arr):
    if n <=0:
        print("Invalid: size must greater than 0")
        return
    for x in arr:
        if x <= 0:
            print("Invalit Input, Greter than 0")
            return
        freq = Counter(arr)
        
        # collect element with even frequency
        result =[]
        for num in arr:
            if freq[num] % 2 ==0 and num not in result:
                result.append(num)
                
        if result:
            for num in result:
                print(num)    
find_even_freq(n, arr)
