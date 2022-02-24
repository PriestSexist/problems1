import random

def MatrSort():
    m = int(input("Введите длину массива"))
    n = int(input("Введите высоту массива"))
    a = [[random.randint(0, 50) for j in range(m)] for i in range(n)]
    print(a)
    for f in range(m - 2, -1, -1):
        i = 0
        j = f
        if (m - f <= min(m,n)):
            s = [0] * (m - f)
        else:
            s = [0] * min(m,n)
        if m - f <= min(m,n):
            while j != m:
                s[i] = a[i][j]
                i = i + 1
                j = j + 1
            s.sort()
            i = 0
            j = f
            while j != m:
                a[i][j] = s[i]
                i = i + 1
                j = j + 1
        else:
            for d in range(min(m,n)):
                s[d] = a[d][j]
                j = j + 1
            s.sort()
            j = f
            for d in range(min(m,n)):
                a[d][j] = s[d]
                j = j + 1


    for f in range(n - 2, 0, -1):
        j = 0
        i = f
        if (n - f <= min(m,n)):
            s = [0] * (n - f)
        else:
            s = [0] * min(m,n)
        if n - f <= min(m,n):
            while i != n:
                s[j] = a[i][j]
                i = i + 1
                j = j + 1
            s.sort()
            j = 0
            i = f
            while i != n:
                a[i][j] = s[j]
                i = i + 1
                j = j + 1
        else:
            for d in range(min(m,n)):
                s[d] = a[i][d]
                i = i + 1
            s.sort()
            i = f
            for d in range(min(m,n)):
                a[i][d] = s[d]
                i = i + 1
    print (a)

MatrSort()