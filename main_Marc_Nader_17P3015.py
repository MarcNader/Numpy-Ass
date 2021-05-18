import numpy as np

def randomization(n):
    """
    Arg:
      n - an integer
    Returns:
      A - a randomly-generated nx1 Numpy array.
    """
    #Your code here
    if n>0 and type(n)==int:
        A=np.random.rand(n,1)
    return A
    
    
n=int(input("Enter a positive number: "))
r=randomization(n)
print(r)
    

def operations(h, w):
    """
    Takes two inputs, h and w, and makes two Numpy arrays A and B of size
    h x w, and returns A, B, and s, the sum of A and B.

    Arg:
      h - an integer describing the height of A and B
      w - an integer describing the width of A and B
    Returns (in this order):
      A - a randomly-generated h x w Numpy array.
      B - a randomly-generated h x w Numpy array.
      s - the sum of A and B.
    """
    #Your code here
     A= np.random.random([h,w]) 
    B=np.random.random([h,w])
    S=A+B
    return A, B, S
h=int(input("Enter heigh value:"))
w=int(input("Enter width value:"))
matriceA, matriceB, Sum=operations(h,w)
print("Matrice A:")
print(matriceA)
print("Matrice B:")
print(matriceB)
print("Sum of matrice A and B:")
print(Sum)


def norm(A, B):
    """
    Takes two Numpy column arrays, A and B, and returns the L2 norm of their
    sum.

    Arg:
      A - a Numpy array
      B - a Numpy array
    Returns:
      s - the L2 norm of A+B.
    """
    #Your code here
    s = np.linalg.norm(A + B)
    return s
A = np.random.random([5,])
B = np.random.random([5,])
output=norm(A,B)
print(output)


def neural_network(inputs, weights):
    """
     Takes an input vector and runs it through a 1-layer neural network
     with a given weight matrix and returns the output.

     Arg:
       inputs - 2 x 1 NumPy array
       weights - 2 x 1 NumPy array
     Returns (in this order):
       out - a 1 x 1 NumPy array, representing the output of the neural network
    """
    #Your code here
    product=np.matmul(weights.transpose(),inputs)
    out=np.tanh(product)
    return out


def scalar_function(x, y):
    """
    Returns the f(x,y) defined in the problem statement.
    """
    #Your code here
    if x<=y:
        return x*y
    else: 
        return x/y

def vector_function(x, y):
    """
    Make sure vector_function can deal with vector input x,y 
    """
    #Your code here
    vectorized = np.vectorize(scalar_function)
    return vectorized(x,y)

x=vector_function(5,5)
print(x)

