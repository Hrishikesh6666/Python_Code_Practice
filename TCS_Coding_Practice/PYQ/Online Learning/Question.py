
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
    
