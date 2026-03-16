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