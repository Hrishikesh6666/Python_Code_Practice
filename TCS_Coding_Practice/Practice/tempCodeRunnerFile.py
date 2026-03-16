def factorial(x):
    if x ==0 and x ==1:
        return 1
    result = 1
    for i in range(2,x+1):
        result *= i
    return result
print(factorial(9)) 