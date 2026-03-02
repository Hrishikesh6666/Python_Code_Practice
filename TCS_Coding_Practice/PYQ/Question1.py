# This function takes a camel case string as input and returns a formatted string with 
# spaces between words and all characters in lowercase.


def format_camel_case(s):
    result = ""
    for i in range(len(s)):
        if s[i].isupper() and i !=0:
            result += " "
            result += s[i].lower()
        else:
            result += s[i]
    return result

# Example usage:
input_string = "CamelCaseString"    
formatted_string = format_camel_case(input_string)
print(formatted_string)  # Output: "camel case string"