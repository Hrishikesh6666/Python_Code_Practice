def max_sum_sliding(arr,k):
    n = len(arr)
    # Sum of the first 
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k,n):
        
        window_sum += arr[i] 
        window_sum  -= arr[i-k]
    
        max_sum = max(max_sum,window_sum)
    return max_sum

arr = list(map(int, input("Enter numbers separated by space: ").split()))
k = 3
print("Maximum Subarray Sum:", max_sum_sliding(arr,k))

