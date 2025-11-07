import sys

input = sys.stdin.readline

N = int(input())
a = []
stack = []
res = 0

for _ in range(N):
    a.append(int(input()))

for x in a:
    if x != 0:
        stack.append(x)
    else:
        stack.pop()

print(sum(stack))
