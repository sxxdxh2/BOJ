def DFS(L, start):

    if L == 6:
        print(*arr)
        return
    else:
        for i in range(start, k):
            arr[L] = s[i]
            DFS(L + 1, i + 1)


if __name__ == "__main__":

    while True:
        k, *s = map(int, input().split())  # 언패킹
        arr = [0] * 6
        if k == 0:
            break
        DFS(0, 0)
        print()
