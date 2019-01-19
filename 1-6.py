# !/usr/bin/env python3

N = 5
a = [2, 3, 4, 5, 10]

# N = 4
# a = [4, 5, 10, 20]


def is_triangle(N, a):
    max = 0
    a_i, a_j, a_k = 0, 0, 0
    for i in range(0, N):
        for j in range(0, N):
            if (j <= i):
                continue
            for k in range(0, N):
                if (k <= j):
                    continue
                if (a[i] + a[j] > a[k]):
                    max = a[i] + a[j] + a[k]
                    a_i, a_j, a_k = a[i], a[j], a[k]
    if (max != 0):
        print("%d(%d,%d,%dの棒を選んだとき)" % (max, a_i, a_j, a_k))
    else:
        print("0(どのように選んでも三角形は作れない)")


is_triangle(N, a)
