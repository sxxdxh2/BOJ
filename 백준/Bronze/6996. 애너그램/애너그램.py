N = int(input())

for _ in range(N):
    w1, w2 = map(str, input().split())
    a = sorted(list(w1))
    b = sorted(list(w2))

    if a == b:
        print(w1, " & ", w2, " are anagrams.", sep="")
    else:
        print(w1, " & ", w2, " are NOT anagrams.", sep="")
