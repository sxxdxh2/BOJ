from collections import deque

N = int(input())

a = list(map(int, range(1, N + 1)))
dq = deque(a)

while len(dq) > 1:

    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])
