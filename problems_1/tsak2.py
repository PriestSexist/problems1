def maxEl(a):
    for i in range(len(a)):
        for j in range(len(a)):
            st1 = a[i]+a[j]
            st2 = a[j]+a[i]
            if st1 > st2:
                a[i], a[j] = a[j], a[i]


a = [str(i) for i in input('Введите числа ').split()]
maxEl(a)
t = ""
for i in range((len(a))):
    t += a[i]
print(t)
