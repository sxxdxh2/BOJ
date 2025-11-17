def DFS(v, total):
    global cnt
    if v == N:
        if total == S:
            cnt += 1
        return
    else:
        DFS(v + 1, total + arr[v])
        DFS(v + 1, total)


if __name__ == "__main__":
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0

    DFS(0, 0)
    if S == 0:
        cnt -= 1

    print(cnt)
