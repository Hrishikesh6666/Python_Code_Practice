## check the string is palindrome or Not

def  is_palindrome(s):
    if s == s[::-1]:
        return "palindrome"
    else:
        return "Not Palendrome"
print(is_palindrome(s="ABCBA"))

## count the number of vowels , consonants,space,digits

def count_characters(s):
    if len(s) == 0:
        return "Invalid Input : Enter the word"
    vowels = 0
    consonants = 0
    digit = 0
    spaces = 0
    
    for ch in s:
        if ch in "aeiouAEIOU":
            vowels += 1
        elif ch.isdigit():
            digit += 1
        elif ch.isalpha():
            consonants += 1
        else:
            spaces += 1
    return vowels,consonants,digit,spaces
s = input("Enter: ")
print(count_characters(s))

## remove all vowels fom string

def remove_vowels(s):
    result =""
    for ch in s:
        if ch not in "aeiouAEIOU":
            result += ch
    return result
s = "aeoiudwnjnnndndj"
print(remove_vowels(s))

#======================  OR ==========


def remove_spaces(s):
    result =""
    for ch in s:
        if not ch.isspace():
            result += ch
    return result
s = "aeoiudwn jnnndndj"
print(remove_spaces(s))

## find the ASCIT Value of the character

c =input("Enter String: ")
ascii_num = ord(c)
print(ascii_num)

## remove character in the string except alphabets
s = input("Enter: ")
def removeNonAlphabets(s):
    result =""
    for ch in s:
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            result += ch
        
    return result
print(removeNonAlphabets(s))

## capitalize first and last character of the words of string

def Capitalize(s):
    result = ""
    for word in s:
        if len(word) == 1:
            new_word = word.upper()
        else:
            new_word = word[0].upper() + word[1:-1] + word[-1].upper()
        result += new_word + " "
    return result.strip()   # remove trailing space

s = input("Enter the string: ").split()
print(Capitalize(s))

## calculate the frequency of string
num = int(input("Enter: "))

def frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    # collect characters that appear exactly 'num' times
    result = [key for key, value in freq.items() if value == num]
    return result

print(frequency("aaaeoiu"))
    