import sys

input = sys.stdin.readline


def DFS(L):
    if L == M:
        print(*arr)
        return
    else:
        for i in range(1, N + 1):
            if ch[i] == 0:
                ch[i] = 1
                arr[L] = i
                DFS(L + 1)
                ch[i] = 0


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [0] * M
    ch = [0] * (N + 1)

    DFS(0)
