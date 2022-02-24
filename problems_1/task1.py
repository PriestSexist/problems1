def Perimeter(a):
    a.sort()
    for i in range(len(a) - 3, -1, -1):
        if a[i] + a[i + 1] > a[i + 2]:
            return a[i] + a[i + 1] + a[i + 2]
    return 0


a = [int(i) for i in input('Введите значения длин через пробел ').split()]
print(Perimeter(a))
