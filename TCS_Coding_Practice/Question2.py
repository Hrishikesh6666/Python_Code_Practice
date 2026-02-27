def eqilibrium_index(arr):
    Total_sum= sum(arr)
    left_sum =0
    
    for i in range(len(arr)):
        right_sum =Total_sum - left_sum - arr[i]
        if left_sum == right_sum:
            return i
        left_sum += arr[i]
    return -1

arr = [0,5,6,3,2]
result = eqilibrium_index(arr)  
print("The equilibrium index is:", result)

# Another way to find eqilibrium index Broteforce approach

def eqilibrium_index_Broteforce(arr):
    for i in range(len(arr)):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i+1:])
        if left_sum == right_sum:
            return i
    return -1

ans = eqilibrium_index_Broteforce(arr)
print("The equilibrium index using brute force is:", ans)