# Example for a palindrome: “madam” — reads the same backward as forward

def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:    
        return False
word = "ramar"
print(is_palindrome(word))