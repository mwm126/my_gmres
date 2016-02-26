import random

NX = 10
NY = 10
NZ = 10
IJK_FIXED = 1

GET_IJK = lambda i, j, k: 1 + k + NZ*(j + NY*i)

fA = open("AA.dat", "w")
fb = open("bb.dat", "w")

for i in range(0, NX):
    print((i, NX))
    for j in range(0, NY):
        for k in range(0, NZ):
            print(random.uniform(-1.0, 1.0), file=fb)
            ijk = GET_IJK(i, j, k)

            if ijk == IJK_FIXED:  # fix one point to make system determinate
                print(ijk, ijk, 1.0, file=fA)
            else:         # build
                centerCoeff = -6.0

                if i == 0:
                    centerCoeff += 1.0
                else:
                    print(ijk, GET_IJK(i-1, j, k), 1.0, file=fA)

                if j == 0:
                    centerCoeff += 1.0
                else:
                    print(ijk, GET_IJK(i, j-1, k), 1.0, file=fA)

                if k == 0:
                    centerCoeff += 1.0
                else:
                    print(ijk, GET_IJK(i, j, k-1), 1.0, file=fA)

                if i == NX-1:
                    centerCoeff += 1.0
                else:
                    print(ijk, GET_IJK(i+1, j, k), 1.0, file=fA)

                if j == NY-1:
                    centerCoeff += 1.0
                else:
                    print(ijk, GET_IJK(i, j+1, k), 1.0, file=fA)

                if k == NZ-1:
                    centerCoeff += 1.0
                else:
                    print(ijk, GET_IJK(i, j, k+1), 1.0, file=fA)

                print(ijk, ijk, centerCoeff, file=fA)

fA.close()
fb.close()
