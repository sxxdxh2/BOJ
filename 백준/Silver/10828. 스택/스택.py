import sys

input = sys.stdin.readline  # 입출력 속도 개선

stack = []

for _ in range(int(input())):  # N 입력만큼 반복
    cmd = input().split()

    if cmd[0] == "push":
        stack.append(cmd[1])

    elif cmd[0] == "pop":
        if not stack:
            print(-1)
        else:
            # stack.pop(cmd[1]) -> XXX
            # pop()은 인덱스가 아니라 맨 위 제거
            print(stack.pop())

    elif cmd[0] == "size":
        print(len(stack))

    elif cmd[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)

    elif cmd[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])