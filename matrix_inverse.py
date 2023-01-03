def zeros_matrix(rows, cols):
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)
    return A

def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])
    MC = zeros_matrix(rows, cols)
    for i in range(rows):
        for j in range(rows):
            MC[i][j] = M[i][j]
    return MC

def determinant(A):
    n = len(A)
    AM = copy_matrix(A)
    for fd in range(n):
        for i in range(fd+1,n):
            if AM[fd][fd] == 0:
                AM[fd][fd] == 1.0e-18
            crScaler = AM[i][fd] / AM[fd][fd]
            for j in range(n):
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
    product = 1.0
    for i in range(n):
        product *= AM[i][i]
    return product

def Identity(size):
    matrix = zeros_matrix(size, size)
    for row in range(0, size):
        for col in range(0, size):
            if (row == col):
                matrix[row][col] = 1
            else:
                matrix[row][col] = 0
    return matrix

def inverse_matrix(x):
    if len(x) == len(x[0]):
        if determinant(x) != 0:
            A_copy = copy_matrix(x)
            I = Identity(len(x))
            I_copy = copy_matrix(I)
            indicates = list(range(len(x)))
            for fd in range(len(x)):
                fdScaler  = 1.0 / A_copy[fd][fd]
                for j in range(len(x)):
                    A_copy[fd][j] *= fdScaler
                    I_copy[fd][j] *= fdScaler
                    for i in indicates[0:fd] + indicates[fd+1:]:
                        crScaler = A_copy[i][fd]
                        for j in range(len(x)):
                            A_copy[i][j] = A_copy[i][j] - crScaler * A_copy[fd][j]
                            I_copy[i][j] = I_copy[i][j] - crScaler * I_copy[fd][j]
            return I_copy
        else:
            print("Bu matrixin determinanti 0 bu sebeple invert edilemez")
    else:
        print("Bu matrix kare değil bu sebeple inverse edilemez")
