def count_character(s):
    if len(s) ==0:
        return("Invalid:len of the string must greater than 0")
    
    vowels = 0
    consonants =0
    digit =0
    special =0
    
    for ch in s:
        if ch in "aeiouAEIOU":
            vowels += 1
        elif ch.isalpha():
            consonants += 1
        elif ch.isdigit():
            digit += 1
        else:
            special += 1
    return vowels,consonants,digit,special
s = input("Enter :")
print(count_character(s))