# Imports the time, numpy and matplot libraries
import time
import numpy
import matplotlib.pyplot as plot

# Exercise 1.a:

# Defines a function which implements the standard matrix multiplication algorithm 
# for two square matrices A and B, returns the result C
def multiplication_of_matrices(A, B):
    # The dimension n is the length of the rows / columns of A (or B)
    n = len(A)
    # Creates a matrix (list) C with 0s as elements
    C = [[0] * n for i in range(n)]
    # Multiplies the elements of A and B
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Eercise 1.c:

# Defines a main function which runs the full program
def main():
    test_and_plot_runtimes()

# Defines a function which determines the runtime of my own matrice multiplication 
# program, which take randomly created matrices of a given dimension and returns the runtime
def runtime_own(dimension):
    # Creates random matrices A and B of a given dimension
    A = [[numpy.random.random() for i in range(dimension)] for j in range(dimension)]
    B = [[numpy.random.random() for i in range(dimension)] for j in range(dimension)]
    # Determines the time of the start of the algorithm
    start_time = time.time()
    # Runs the multiplication
    C = multiplication_of_matrices(A, B)
    # Determines the time of the end of the algorithm
    end_time = time.time()
    # Calculates the runtime
    runtime = end_time - start_time
    print(runtime)
    return runtime

# Defines a function which determines the runtime of numpy's matrice multiplication 
# program, which take randomly created matrices of a given dimension and returns the runtime
def runtime_numpy(dimension):
    # Creates random matrices A and B of a given dimension
    A = numpy.random.rand(dimension, dimension)
    B = numpy.random.rand(dimension, dimension)
    # Determines the time of the start of the algorithm
    start_time = time.time()
    # Runs the multiplication
    C = numpy.dot(A, B)
    # Determines the time of the end of the algorithm
    end_time = time.time()
    # Calculates the runtime
    runtime = end_time - start_time
    print(runtime)
    return runtime

# Defines a function which tests both my own and numpys matrix multiplication algorithm's runtime
# and plots a graph with each runtime
def test_and_plot_runtimes():
    # List of the dimensions n of matrices A and B
    dimensions = range(1, 1001, 333)
    # Lists of runtimes 
    own_runtimes = []
    numpys_runtimes = []

    print("\nCalculating the Products of matrices of different dimensions, this might take a while...\n",
          "Please wait until the runtime graphs are plotted!")

    # Determines the runtimes for the multiplication of different dimensions n matrices A and B
    # for my own algorithm and numpys and appends the runtimes to lists
    for dimension in dimensions:
        own_runtimes.append(runtime_own(dimension))
        numpys_runtimes.append(runtime_numpy(dimension))

    print(own_runtimes, numpys_runtimes)
    # Plots the results from the runtime lists
    plot.plot(dimensions, own_runtimes, label="Own algorithm", marker='o')
    plot.plot(dimensions, numpys_runtimes, label="NumPy's dot product", marker='o')
    plot.xlabel("Dimension n")
    plot.ylabel("Runtime in seconds")
    plot.title("Matrix multiplication runtime: own vs. numpy's algorithm")
    plot.legend()
    plot.grid()
    plot.show()

# Calls the main function (if not imported)
if __name__ == "__main__":
    main()
