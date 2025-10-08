n = int(input())
x = []
y = []
aa = bb = 100

for i in range(n):

    a, b = map(int, input().split())

    x.append(a)
    y.append(b)

    if x[i] < y[i]:
        aa -= int(y[i])
    elif x[i] > y[i]:
        bb -= int(x[i])

print(aa)
print(bb)
