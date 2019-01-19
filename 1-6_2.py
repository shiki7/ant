# !/usr/bin/env python3

L = 10
n = 3
x = [2, 6, 7]


def getMin(L, n, x):
    min = 0
    direction = ['', '', '']
    for i in range(0, 3):
        if (x[i] <= L - x[i]):
            direction[i] = '左'
            if x[i] > min:
                min = x[i]
        else:
            direction[i] = '右'
            if L - x[i] > min:
                min = L - x[i]
    print("min=%d(%s、%s、%s)" % (min, direction[0], direction[1], direction[2]))


# maxを求める場合、端から最も遠いアリを求める。すべてのアリがその方向と同じ方向に動くと定義できる
def getMax(L, n, x):
    max = 0
    direction = ''
    for i in range(0, 3):
        if (x[i] < L - x[i]):
            if L - x[i] > max:
                direction = '右'
                max = L - x[i]
        else:
            if x[i] > max:
                direction = '左'
                max = x[i]
    print("max=%d(%s、%s、%s)" % (max, direction, direction, direction))


getMin(L, n, x)
getMax(L, n, x)
