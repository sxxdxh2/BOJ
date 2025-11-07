import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    s = input().strip()

    for x in s:
        if x == "(":
            stack.append("(")
        else:
            if not stack:
                print("NO")
                break
            stack.pop()
    else:
        print("YES" if not stack else "NO")
    stack.clear()
