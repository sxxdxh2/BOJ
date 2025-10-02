t = int(input())

for i in range(t):

    a = input().split()
    sum = float(a[0])

    for k in a[1:]:

        if k == "@":
            sum *= 3
        elif k == "%":
            sum += 5
        elif k == "#":
            sum -= 7

    print(f"{sum:.2f}")
