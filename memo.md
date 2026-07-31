# 整数1個
n = int(input())

# 文字列1個
s = input()

# 整数がスペース区切りで複数
a, b = map(int, input().split())

# 2桁で0埋めして出力
result = f"{ans:02d}"

#　回答を完了したらgitに追加
git add .
git commit -m "Solve ABC003 A"
git push