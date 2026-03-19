num = int(input("Enter: "))

def frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    # collect characters that appear exactly 'num' times
    result = [key for key, value in freq.items() if value == num]
    return result

print(frequency("aaaeoiu"))