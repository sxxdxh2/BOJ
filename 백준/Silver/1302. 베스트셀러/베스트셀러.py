N = int(input())
s = {}

for _ in range(N):
    word = input()
    if word not in s:
        s[word] = 1
    else:
        s[word] += 1

max_cnt = max(s.values())

res = [k for k, v in s.items() if v == max_cnt]
res.sort()  # 사전 순으로 정렬
print(res[0])
