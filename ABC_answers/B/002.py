S = list(input())
result = []
for i in S:
    if i not in "aiueo":
        result.append(i)

ans = "".join(result)
print(ans)
