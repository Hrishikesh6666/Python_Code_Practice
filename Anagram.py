str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# checking the length of the strings
if len(str1) != len(str2):
    print("The strings are not anagrams.")
else:
    # sorting the characters of the strings
    if sorted(str1) == sorted(str2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")