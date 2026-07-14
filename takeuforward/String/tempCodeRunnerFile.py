
num = int(input("Enter the frequency: "))

def frequency(s):
    freq = {}
    
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    result = [key for key, value in freq.items() if value == num]
    return result

print(frequency("aaaeoiu"))