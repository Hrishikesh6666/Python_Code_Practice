print("Reverse a Number")
num = int(input("Enter a number: "))
rev = 0
while num >0:
    rev = num  % 10 + rev * 10
    num =num //10
print(f"Reverse of the number is: {rev}")
    
# USING STRING SLICING
Print="Reverse a Number using String Slicing"
number =input("Enter a number: ")
rev =(number)[::-1]
print(f"Reverse of the number is using string slicing: {rev}")