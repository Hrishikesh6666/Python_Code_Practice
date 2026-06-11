def rotate_matrix(matrix,N):
    ## Transpose matrix
    for i in range(N):
        for j in  range(1,N):
            matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # step2: reverse each row
    
    for i in range(N):
        matrix[i].reverse()
    return matrix

N = int(input("Enter : "))
matrix = []
for _ in range(N):
    row = list(map(int,input("enter the number: ").split( )))
    matrix.append(row)
print(rotate_matrix(matrix,N))


def rotate_matrix(N):
    for i in range(N):
        for j in range(N):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    
    for i in range(N):
        matrix[i].reverse()
    return matrix

N = int(input("Enter :"))
matrix=[]

for _ in range(N):
    row = list(map(int,input("Enter in row: ").split( )))
    matrix.append(row)
print(rotate_matrix(N))
