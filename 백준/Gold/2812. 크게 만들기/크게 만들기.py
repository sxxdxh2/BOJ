N, K = map(int, input().split())
num = list(map(int, input().strip()))  # input()까지만 하면 \n이 붙음 (문자열)
stack = []

for x in num:
    while stack and K > 0 and stack[-1] < x:
        stack.pop()
        K -= 1
    stack.append(x)

if K > 0:
    stack = stack[:-K]

res = "".join(map(str, stack))
print(res)
