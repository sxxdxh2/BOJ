def DFS(L):
    if L == M:
        print(*arr)
        return

    for i in range(1, N + 1):
        arr[L] = i
        DFS(L + 1)


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [0] * M
    DFS(0)