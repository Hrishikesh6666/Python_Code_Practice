def find_firstcharacter(s,p):
    freq = {}
    
    for ch in s:
        freq[ch] = freq.get(ch,0)+1
        
    result = []
    for ch in freq:
        if freq[ch] >= p:
            result.append(ch)
    return min(result)

s = input()
p = int(input())
print(find_firstcharacter(s,p))
   
from collections import Counter

def find_firstcharacter(s,p):
    freq = Counter(s)
    
    result =[ch for ch,value in freq.items() if freq[ch] >= p]
    print(min(result))
print(find_firstcharacter(s,p))