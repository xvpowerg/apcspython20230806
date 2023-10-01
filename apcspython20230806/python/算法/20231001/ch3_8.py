def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

def flipMatrix(matrixA):
    matrixB = []
    r = len(matrixA)
    for i in range(r-1,-1,-1):
        matrixB.append(matrixA[i])
    return matrixB
        
m1 = [[3,6],
      [2,5],
      [1,4]]
printMatrix(m1)
print("==============")
m2 = flipMatrix(m1)
printMatrix(m2)




