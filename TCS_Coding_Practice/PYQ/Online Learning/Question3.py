def count_characters(s):
    if len(s) ==0:
        print("Invalid: string length must greater than 0")
        return
    
    vowels =0
    consonants =0
    digits = 0
    special =0
    # classify each character:
    
    for ch in s:
        if ch in 'aeoiuAEIOU':
            vowels +=1
        elif ch.isalpha():
            consonants +=1
        elif ch.isdigit():
            digits +=1
        else:
            special +=1
    return vowels,consonants,digits,special

s = input("Enter String:")
print(count_characters(s))
    