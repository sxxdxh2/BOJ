n = int(input())
p = []

for i in range(n):
    a, b, c = map(int, input().split())

    if a == b == c:
        p.append(10000 + a * 1000)
    elif a == b or a == c:
        p.append(1000 + a * 100)
    elif b == c:
        p.append(1000 + b * 100)
    else:
        p.append(max(a, b, c) * 100)

print(max(p))