import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    cmd = input().split()

    if cmd[0] == "1":
        stack.append(cmd[1])

    elif cmd[0] == "2":
        if stack:
            print(stack.pop())  # pop한 값을 출력
        else:
            print(-1)

    elif cmd[0] == "3":
        print(len(stack))

    elif cmd[0] == "4":
        print(1 if not stack else 0)

    elif cmd[0] == "5":
        print(stack[-1] if stack else -1)
