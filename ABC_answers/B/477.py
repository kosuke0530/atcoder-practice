N, D = map(int, input().split())
X = list(map(int, input().split()))

ans = []

for i in range(N):
    is_valid = True
    for j in range(N):
        if i == j:
            continue  # 自分自身との比較はスキップ
        if abs(X[i] - X[j]) < D:
            is_valid = False
            break
            
    if is_valid:
        ans.append(X[i])

if not ans:
    print(0)
    print('')
else:
    print(len(ans))
    print(*ans)  # リストの中身を空白区切りで出力