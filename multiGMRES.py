""" this is a multi-basis vector version of GMRES"""

import csv
from scipy.io import loadmat
import scipy.sparse
from numpy import diag, zeros
from numpy.linalg import inv, norm, det

def multiGMRES():
    "multi basis vector GMRES variant"

    print("Loading AA matrix")

    # AA = loadmat('AA.dat')

    AA = scipy.sparse.dok_matrix((100000,100000))

    csvreader = csv.reader(open('AA.dat'), delimiter=' ', skipinitialspace=True)
    for line in csvreader:
        row, column, val = line[:3]
        AA[int(row),int(column)] = float(val)
        # print(row, column, val)
        # AA.data[row].append(column)

    exit
    print("Converting AA matrix\n")
    # AA = spconvert(AA)
    # AA = sparse(i,j,val)
    print("AA Matrix ready\n")

    print(AA)

    bb = loadmat('bb.dat')

    xx = np.zeros(len(bb, 1), 1)
    MM = scipy.sparse.identity(len(bb))

    print(len(AA))
    print(len(xx))
    print(len(bb))

    print("Building Krylov space")

    MM = inv(diag(diag(AA)))

    print(MM)

    krylovSpaceNorms( AA, xx, bb, MM, 10)

    # print (xx)
    # print (A*xx - b)
    # print norm(A*xx - b)

def krylovSpaceNorms( A, x, b, M, n ):
    "do multiGMRES"

    k = []

    bNorm = norm(b)
    print("Initial Residual: %e\n",norm(A*x - b)/bNorm)


    for _ in range(0, 100):

        res = b - A*x

        k[1] = res

        # printf ( '%d, %e\n',1,norm(k{1}))
        for i in range( 2, n+1 ):
            t = M*k[i-1]
            k[i] = A*t
            # print( '%d, %e\n',i,norm(k{i}))

        # print("Building dot product matrix\n")

        for i in range( 2, n+1 ):
            r[i-1] = dot(k[i],res)
            for j in range( 2, n+1 ):
                N[i-1,j-1] = dot(k[i],k[j])

        print(det(N))
        print(N)
        print(r.transpose())

        # alpha = N \ r'

        print(alpha)

        err = N*alpha - r
        # print (norm(err))

        # dalpha = N \ (err)
        # alpha -= dalpha
        # err = N*alpha - r'
        # print (norm(err))

        # dalpha = N \ (err)
        # alpha -= dalpha
        # err = N*alpha - r'
        # print (norm(err))

        y = zeros(len(x))
        for i in range( 1, n ):
            y += alpha(i)*k[i]
        x += M*y

        print (norm(A*x-b)/bNorm)
        # print(x)

if __name__ == '__main__':
    multiGMRES()
