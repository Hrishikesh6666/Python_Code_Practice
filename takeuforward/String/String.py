def is_palindrome(s):
    
    if s == s[:: -1]:
        return True
    else:
        return False
print(is_palindrome("madam"))

def remove_vowels(s):
    result = ""
    for char in s:
        if char not in "aeiouAEIOU":
            result += char
        return result
print(remove_vowels("hello world"))

## remove character in the string except alphabets

def remove_non_alphabets(s):
    result =""
    for ch in s:
        if ch.isalpha():
            result += ch
    return result
print(remove_non_alphabets("hello123world"))

## calculate the frequency of string

num = int(input("Enter the frequency: "))

def frequency(s):
    freq = {}
    
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    result = [key for key, value in freq.items() if value == num]
    return result

print(frequency("aaaeoiu"))


def remove_spaces(s):
    result =""
    for ch in s:
        if not ch.isspace():
            result += ch
    return result
s = "aeoiudwn jnnndndj"
print(remove_spaces(s))
