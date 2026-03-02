def toggle_bits(N):
    
    binary = bin(N)[2:]  # Convert to binary and remove the '0b' prefix
    toggled =""
    for bit in binary:
        if bit == "1":
            toggled += "0"
        else:
            toggled += "1"
    return int(toggled, 2)

# Read input
N = int(input("Enter the number: ").strip())
# Get the toggled result
result = toggle_bits(N) 
# Print the result
print(result)


# =================================OR ================================

def toggle_bits(N):
    
    k = N.bit_length()  # Get the number of bits needed to represent N
    mask = (1 << k) - 1  # Create a mask with k bits set to 1
    toggled = N ^ mask  # Toggle the bits using XOR with the mask
    return toggled



'''Line-by-Line Explanation

def toggle_bits(N):

Defines a function named toggle_bits that takes one input, N (an integer).

binary = bin(N)[2:]

bin(N): Converts the integer N into a binary string. For example, bin(5) returns '0b101'.

[2:]: This is a string slice. It removes the first two characters ('0b'), leaving only the actual binary digits (e.g., '101').

toggled = ""

Initializes an empty string called toggled to store the new bits as we flip them.

for bit in binary:

Starts a loop that looks at every character (0 or 1) in the binary string one by one.

if bit == '1':

Checks if the current bit is a '1'.

toggled += '0'

If it was a '1', we add a '0' to our toggled string.

else:

If the bit was not a '1' (meaning it was a '0').

toggled += '1'

We add a '1' to our toggled string.

return int(toggled, 2)

int(toggled, 2): Converts the finished toggled string back into a base-10 integer. The 2 tells Python the input string is in binary.'''