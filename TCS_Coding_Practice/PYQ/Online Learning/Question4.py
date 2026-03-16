N = int(input("Enter size: "))
arr = [int(input()) for _ in range(N)]

count = [0] * 4   # assuming values are only 0,1,2,3

for x in arr:
    count[x] += 1

for i in range(4):
    for _ in range(count[i]):
        print(i)
    
