def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

matrixA = []
for i in range(2):
    row = []
    for j in range(3):
        row.append((i+1)**2+(j+1)**2)
    matrixA.append(row)

printMatrix(matrixA)
