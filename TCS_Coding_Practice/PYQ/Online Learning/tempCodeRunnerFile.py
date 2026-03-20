        
N = int(input("Enter size: "))
arr = list(map(int, input("Enter numbers: ").split()))
    
def sorted_arr(arr):
    count = [0,0,0,0]
    for num in arr:
        count[num] += 1
    
    result =[]
    for num in range(4):
        result.extend([num]*count[num])
    return result
print(sorted_arr(arr))