s = input().strip()
stack = []
ans = 0

for i, ch in enumerate(s):  # i : 순서, ch : (,)
    if ch == "(":
        stack.append("(")  # ( 를 stack에 추가
    else:  # ch == ')'
        stack.pop()  # 이전 ( 중 하나가 닫힘
        if s[i - 1] == "(":  # 바로 앞이 ( 면
            ans += len(stack)  # 막대 수 만큼 잘림
        else:  # 바로 앞이 ) -> 막대 끝
            ans += 1  # 마지막 조각 +1

print(ans)
