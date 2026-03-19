def even_frequency(arr):
    N = len(arr) 
    freq ={}
    
    for num in arr:
        freq[num] = freq.get(num,0)+1
        
    
    even_frequency_result =[num for num,value in freq.items()if value  % 2 == 0 ]
    if not even_frequency_result:
        return "No even frequency present in the arr"
    return even_frequency_result

N = int(input("Length arr : "))
arr = list(map(int,input("Enter elemnet in the arr: ").split( )))
print (even_frequency(arr))

## =========================== or ==============
from collections import Counter

def even_freq(arr):
    N = len(arr)
    
    if N <=0:
        return "invalid : size of the length of arr"
    for x in arr:
        if x <= 0:
            return "Invalid : elemnet must be greater than 0"
        
        # count the frequency
        freq =Counter(arr)
        
        # collect element with even frequency
        result =[]
        for num in arr:
            if freq[num] % 2 == 0 and num not in result:
                result.append(num)
        return result
    
print(even_freq(arr))

        