N = int(input())
a = input()

values = {}

for i in range(N):
    num = int(input())
    values[chr(ord("A") + i)] = num  # values[key] = value
    # char(65) = 'A', char(66) = 'B', ...

# values = { 'A': 1, 'B': 2, ... }

stack = []

for x in a:
    if x.isalpha():
        stack.append(values[x])
    else:
        right = stack.pop()
        left = stack.pop()
        if x == "+":
            stack.append(left + right)
        elif x == "-":
            stack.append(left - right)
        elif x == "*":
            stack.append(left * right)
        elif x == "/":
            stack.append(left / right)

print(f"{stack[0]:.2f}")
