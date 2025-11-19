import itertools as it

while True:
    k, *s = map(int, input().split())
    arr = [0] * 6
    if k == 0:
        break

    for x in it.combinations(s, 6):
        print(*x)

    print()
