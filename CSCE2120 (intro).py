A = [
    [2,-3,5],
    [1,0,-1],
    [0,0,0]
]
B = [
    [3,2,3],
    [-1,1,3],
    [0,0,3]
]
#Vector_ADD
m_add = []
for row in range (len(A)):
    n_add = []
    for ind in range(len(A)):
        n_add.append(A[row][ind] + B [row][ind])
    m_add.append(n_add)
    
print (m_add)
#Vector multiplication
XV = [
    [2,-3,5],
    [1,0,-1],
    [0,0,0]
]
Y = [
    [3,2],
    [-1,3],
    [0,0]
]
mult_mat=[]
for row in range(len(XV)):
    step_mat = []
    for column in range(len(Y[0])):
        total = 0
        for k in range (len(XV[0])):
            total += XV[row][k]*Y[k][column]
        step_mat.append(total)
    mult_mat.append(step_mat)
print (mult_mat)
