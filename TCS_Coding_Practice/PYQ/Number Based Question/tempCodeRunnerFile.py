def armstrong(num):
    original = num
    total = 0
    
    while num > 0:
        digit = num % 10
        total += digit ** 3
        num //= 10
    
    if total == original:
        return "Armstrong Number"
    else:
        return "Not Armstrong Number"

num = int(input("Enter: "))
print(armstrong(num)) 