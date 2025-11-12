word = input().strip().upper()
s = {}

for ch in word:
    if ch in s:
        s[ch] += 1
    else:
        s[ch] = 1

max_value = max(s.values())

res = [k for k, v in s.items() if v == max_value]
print(res[0] if len(res) == 1 else "?")