# First not repetaing character in a string

def first_non_repeating_character(s):
    feq={}
    
    #count the frequency of each character in the string
    for char in s:
        feq[char]=feq.get(char,0)+1
        
    #find the first non-repeating character
    for char in s:
        if feq[char]==1:
            return char
    return -1

s = "leetcode"
result = first_non_repeating_character(s)  
print(result)  

def first_non_repeating(s):
    for i in range(len(s)):
        if s.count(s[i])==1:
            return s[i]
    return -1

s = "loveleetcode"
ans = first_non_repeating(s)
print(ans)


from collections import Counter
def anothet_way(s):
    
    count = Counter(s)
    
    for char in s:
        if count[char]==1:
            return char
    return -1