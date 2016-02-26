""" this is a multi-basis vector version of GMRES"""

import csv
import scipy.sparse
from numpy import diag, zeros, zeros_like, loadtxt, array, matrix, dot
from numpy.linalg import inv, norm, det, solve

def multiGMRES():
    "multi basis vector GMRES variant"

    print("Loading matrices...")

    rows = []
    cols = []
    vals = []

    # AA = scipy.sparse.dok_matrix((100000, 100000))
    csvreader = csv.reader(open('AA.dat'), delimiter=' ', skipinitialspace=True)
    for line in csvreader:
        row, column, val = line[:3]
        rows.append(int( row ))
        cols.append(int( column ))
        vals.append(float( val ))
        # AA[int(row), int(column)] = float(val)

    rows = array(rows)-1
    cols = array(cols)-1
    vals = array(vals)
    AA = scipy.sparse.coo_matrix((vals,( rows, cols )))
    AA = AA.tocsr()

    bb = loadtxt(open('bb.dat'))
    nn = len(bb)

    bb = matrix(bb).transpose()

    print("Matrices loaded.")

    xx = zeros((len(bb),1))
    MM = scipy.sparse.identity(len(bb))

    print("Building Krylov space")
    inv_diag = 1./AA.diagonal()
    MM = scipy.sparse.spdiags(inv_diag, [0,], nn, nn)

    krylovSpaceNorms(AA, xx, bb, MM, 10)

def krylovSpaceNorms(A, x, b, M, n):
    "do multiGMRES"

    k = []
    nn = len(b)
    for _ in range(n+1):
        kvec = array((nn, 1))
        kvec.fill(333333.)
        k.append(kvec)

    bNorm = norm(b, ord=2)

    print("Initial Residual: ", norm(A*x - b)/bNorm)

    for _ in range(0, 100):

        print("ITERATION ", _)

        res = b - A*x

        # construct n+1 krylov vectors, not using the first to make N
        k[0] = res

        for i in range(1, n+1):
            print("i = ", i)
            t = M*k[i-1]
            k[i] = A*t

        print("Building dot product matrix\n")

        r = zeros(n)
        r.fill(4444444.)
        N = zeros((n, n))
        N.fill(8888888.)
        for i in range(1, n+1):
            r[i-1] = dot(k[i].transpose(), res)
            for j in range(1, n+1):
                N[i-1, j-1] = dot(k[i].transpose(), k[j-1])

        alpha = solve(N, r)

        # err = N*alpha - r
        # dalpha = solve(N, err)
        # alpha -= dalpha
        # err = N*alpha - r.transpose()

        y = zeros_like(x)
        for i in range(1, n):
            y += alpha[i]*k[i]
        x += M*y

        print(norm(A*x-b)/bNorm)

multiGMRES()
