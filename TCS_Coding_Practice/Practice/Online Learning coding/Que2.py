N = int(input("Enter the Num: "))
def toggle_bits(N):
    if N <= 0:
        return "Invalid : N must greater than 0 "
    
    toggle =""
    binary = bin(N)[2:]
    
    for bit in binary:
        if bit == '0':
            toggle += '1'
        else:
            toggle += '0'
    return int(toggle,2)
print(toggle_bits(N))