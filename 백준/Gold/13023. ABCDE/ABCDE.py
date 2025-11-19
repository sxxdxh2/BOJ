import sys

input = sys.stdin.readline


def DFS(node, depth):

    if depth == 5:
        print(1)
        exit(0)

    ch[node] = True

    for x in g[node]:
        if not ch[x]:
            DFS(x, depth + 1)

    ch[node] = False


N, M = map(int, input().split())
g = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

ch = [False] * N

for i in range(N):
    DFS(i, 1)

print(0)
