import numpy as np 

def matrixMul(A,B):
    m=A.shape #find dimensions of the matrices 
    n=B.shape
    if(m[1]!=n[0]): #if number of columns of A is different than the number of rows of B, multiplication is undefined
        print("Cannot perform multiplication")
        return 
    C = np.ndarray(shape=(m[0],n[1]))
    for i in range(m[0]): #for every row of A
        for j in range(n[1]): #for every col of B
            temp = 0
            for l in range(len(B)): #for every element in row of A and col of B respectively
                temp += A[i,l]*B[l,j]  #add to product the product of the elements A[i,l] and B[l,j]
                C[i,j]=temp  #put final product to C[i,j] position

    return C




A = np.array([(1,2), (0,-1), (1,-3)])
B = np.array([(-1,0,5), (0,1,-2)])
C = np.array([(1,-2), (-1,1)])

print(matrixMul(A,B))#A*B
print(matrixMul(B,C))#B*C
print(matrixMul(C,C))#C^2
