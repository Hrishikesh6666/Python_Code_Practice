def sort_rank(arr):
    count =[0,0,0,0]
    
    for num in arr:
        count[num] += 1
        
    result= []
    for i in range(4):
        result.extend([i]*count[i])
    return result
    # for i in range(4):
    #     for _ in range(count[i]):
    #         print(i)

arr = list(map(int,input("Enter Num: ").split( )))
print(sort_rank(arr))