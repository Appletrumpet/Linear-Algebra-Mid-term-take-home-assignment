# Imports the time module and numpy
import time
import numpy
import own_and_numpy_matrix_multiplication as multiplication

# Exercise 1.e (Code):

# Defines a main function which runs the full program
def main():
    test_all_runtimes()

# Defines a function which calculates the sum of two matrices
def matrix_addition(A, B):
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(A[0])):
            C[i].append(A[i][j] + B[i][j])
    return C

# Defines a function which calculates the difference of two matrices
def matrix_subtraction(A, B):
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(A[0])):
            C[i].append(A[i][j] - B[i][j])
    return C

# Defines a function, which performs the strassens algorithm with recursion
def strassens_recursive(A, B):
    # Divides the matrices into 4 quadrants
    n = len(A)
    middle = n // 2

    # Base case for recursion
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    # Matrix A into 4 quadrants
    A11 = [a[:middle] for a in A[:middle]]
    A12 = [a[middle:] for a in A[:middle]]
    A21 = [a[:middle] for a in A[middle:]]
    A22 = [a[middle:] for a in A[middle:]]
    # Matrix B into 4 quadrants
    B11 = [b[:middle] for b in B[:middle]]
    B12 = [b[middle:] for b in B[:middle]]
    B21 = [b[:middle] for b in B[middle:]]
    B22 = [b[middle:] for b in B[middle:]]

    # Computes 7 products M (instead of 8)
    # M1 = (A11 + A22) x (B11 + B22)
    M1 = strassens_recursive(matrix_addition(A11, A22), matrix_addition(B11, B22))
    # M2 = (A21 + A22) x B11
    M2 = strassens_recursive(matrix_addition(A21, A22), B11)
    # M3 = A11 x (B12 - B22)
    M3 = strassens_recursive(A11, matrix_subtraction(B12, B22))
    # M4 = A22 x (B21 - B11)
    M4 = strassens_recursive(A22, matrix_subtraction(B21, B11))
    # M5 = (A11 + A12) x B22
    M5 = strassens_recursive(matrix_addition(A11, A12), B22)
    # M6 = (A21 - A11) x (B11 + B12)
    M6 = strassens_recursive(matrix_subtraction(A21, A11), matrix_addition(B11, B12))
    # M7 = (A12 - A22) x (B21 + B22)
    M7 = strassens_recursive(matrix_subtraction(A12, A22), matrix_addition(B21, B22))
    
    # Computes the resulting matrix C out of Ms
    C11 = matrix_addition(matrix_subtraction(matrix_addition(M1, M4), M5), M7)
    C12 = matrix_addition(M3, M5)
    C21 = matrix_addition(M2, M4)
    C22 = matrix_addition(matrix_subtraction(matrix_addition(M1, M3), M2), M6)

    # Creates the matrix C (in list form) out of C11, C12, C21 and C22
    C = []
    for i in range(middle):
        C.append(C11[i] + C12[i])
    for i in range(middle):
        C.append(C21[i] + C22[i])
    
    return C

# Defines a function which performs the strassens algorithm without recursion
# for 2x2 matrices
def strassens_non_recursive(A, B):
    # Splits the matrix A into 4 quadrants
    A11 = A[0][0]
    A12 = A[0][1]
    A21 = A[1][0]
    A22 = A[1][1]
    # Splits the matrix B into 4 quadrants
    B11 = B[0][0]
    B12 = B[0][1]
    B21 = B[1][0]
    B22 = B[1][1]

    # Since the quadrants are 1x1 matrices, we don't need
    # to use functions to add / subtract them but can calculate the M matrices
    # directly
    M1 = (A11 + A22) * (B11 + B22)
    M2 = (A21 + A22) * B11
    M3 = A11 * (B12 - B22)
    M4 = A22 * (B21 - B11)
    M5 = (A11 + A12) * B22
    M6 = (A21 - A11) * (B11 + B12)
    M7 = (A12 - A22) * (B21 + B22)

    # Compute the quadrants of the resulting matrix C
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    C = [[C11, C12], [C21, C22]]
    return C

# Defines a function which determines the runtime of my strassens algorithm multiplication 
# program, which take randomly created matrices of a given dimension and returns the runtime
def runtime_strassens(dimension):
    # Creates random matrices A and B of a given dimension
    A = [[numpy.random.random() for i in range(dimension)] for j in range(dimension)]
    B = [[numpy.random.random() for i in range(dimension)] for j in range(dimension)]

    # Determines the runtime of the recursive algorithm
    # Determines the time of the start of the algorithm
    recursive_start_time = time.time()
    # Runs the multiplication
    C = strassens_recursive(A, B)
    # Determines the time of the end of the algorithm
    recursive_end_time = time.time()
    # Calculates the runtime
    recursive_runtime = recursive_end_time - recursive_start_time

    # Determines the runtime of the non-recursive algorithm
    # Determines the time of the start of the algorithm
    non_recursive_start_time = time.time()
    # Runs the multiplication
    C = strassens_non_recursive(A, B)
    # Determines the time of the end of the algorithm
    non_recursive_end_time = time.time()
    # Calculates the runtime
    non_recursive_runtime = non_recursive_end_time - non_recursive_start_time

    return recursive_runtime, non_recursive_runtime

# Defines a function which lets you compare all runtimes for the different algorithms
# for 2x2 matrices
def test_all_runtimes():
    strassens_recursive_runtime, strassens_non_recursive_runtime = runtime_strassens(2)
    own_runtime = multiplication.runtime_own(2)
    numpy_runtime = multiplication.runtime_numpy(2)
    print(f"Runtimes for determining the product of 2x2 matrices:")
    print(f"Strassen's recursive: {strassens_recursive_runtime}")
    print(f"Strassen's non-recursive: {strassens_non_recursive_runtime}")
    print(f"Own: {own_runtime}")
    print(f"NumPy: {numpy_runtime}\n")

# Calls the main function (if not imported)
if __name__ == "__main__":
    main()