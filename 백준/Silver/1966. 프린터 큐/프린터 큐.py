from collections import deque

t = int(input())

for _ in range(t):
    N, M = map(int, input().split())
    prior = list(map(int, input().split()))
    dq = deque([(i, p) for i, p in enumerate(prior)])
    cnt = 0

    while dq:
        cur = dq.popleft()
        if any(cur[1] < other[1] for other in dq):
            dq.append(cur)
        else:
            cnt += 1
            if cur[0] == M:
                print(cnt)
                break
