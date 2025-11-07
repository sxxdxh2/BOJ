import sys
input = sys.stdin.readline

N = int(input())
h = []

for _ in range(N):
    h.append(int(input()))

last = h[-1]
cnt = 1

for i in reversed(range(N)):
    if h[i] > last:
        cnt += 1
        last = h[i]

print(cnt)
