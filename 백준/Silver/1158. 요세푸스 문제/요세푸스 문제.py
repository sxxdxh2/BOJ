from collections import deque  # 양쪽에서 append/pop 가능

N, K = map(int, input().split())
dq = deque(list(range(1, N + 1)))

yosephus = []

while len(dq) > 0:

    for _ in range(K - 1):
        cur = dq.popleft()
        dq.append(cur)
    yosephus.append(dq[0])
    dq.popleft()

print("<", end="")
print(", ".join(map(str, yosephus)), end="")
print(">")
