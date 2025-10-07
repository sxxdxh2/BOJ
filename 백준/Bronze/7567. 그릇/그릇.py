sum = int(10)

s = list(input())

for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        sum += 10
    else:
        sum += 5

print(sum)
