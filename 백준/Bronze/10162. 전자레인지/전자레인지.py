a = 300
b = 60
c = 10

t = int(input())

if t >= a:
    x = t // a
    if (t - a * x) >= b:
        y = (t - a * x) // b
    else:
        y = t - a * x

    if (t - a * x - b * y) >= c:
        z = (t - a * x - b * y) // c
    else:
        z = t - a * x - b * y

elif b <= t < a:
    x = 0
    y = t // b
    if (t - b * x) >= c:
        z = (t - b * y) // c
    else:
        z = t - b * y

elif t < b:
    x = 0
    y = 0
    z = t // c

if (x * a + y * b + z * c) == t:
    print(f"{x} {y} {z}")
else:
    print(-1)
