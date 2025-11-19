def DFS(L, s):

    if L > M:
        return

    if L == M:
        print(*arr)
        return
    else:
        for i in range(s, N + 1):
            arr[L] = i
            DFS(L + 1, i + 1)


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [0] * M
    DFS(0, 1)
