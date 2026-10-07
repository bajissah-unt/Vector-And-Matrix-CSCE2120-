A = [
    [1,2,3],
    [2,3,4],
    [5,6,7]
]
B = [
    [1,0,0],
    [2,45,6]
    [-5,23,1]
]
def check_dim(mat1,mat2):
    if len(mat1)==len(mat2) and len (mat1[0] ) == len (mat2[0]):
        return True
    else:
        print ("not equal components of both the matrix")
def check_size(mat1,mat2):
    if len(mat1[0]) == len (mat2):
        return True

def add_mat(mat1,mat2):
    if check_dim(mat1,mat2):
        added_mat = []
        for row in range (len (mat1)):
            row_sum= []
            for column in len (mat1[0]):
                sum_process = mat1[row][column] + mat2[row][column]
                row_sum.append(sum_process)
            added_mat.append(row_sum)
        print ("The sum of both matrix is = "; added_mat)
    else:
        print ("Invalid dimension or component size")
def mult_mat(mat1,mat2):
    if check_size(mat1,mat2):
        mult_mat = []
        for row in range (len(mat1)):
            row_process = []
            for column in range (len (mat2):
                for k in range (len ( mat2[0])):
                    raw_proc += mat1[row][k]* mat2[k][column]
                row_process.append(rw_proc)
            mult_mat.append(row_process)
        print ("The resulting multiplication = ";mult_mat)
    else:
        print ("Invalid dimension")

add_mat(A,B)
mult_mat(A,B)



                    
        
            
        
    
        
