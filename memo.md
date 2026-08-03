# 整数1個
n = int(input())

# 文字列1個
s = input()

# 整数がスペース区切りで複数
a, b = map(int, input().split())

# 2桁で0埋めして出力
result = f"{ans:02d}"

# リストの要素を区切り文字なし（""）で結合する
ans = "".join(result_list)

切り捨て: a // b
切り上げ: -(-a // b)

# インデックスメソッドでインデックスの出力
l = [30, 50, 10, 40, 20]
print(l.index(30))

#　回答を完了したらgitに追加
git add .
git commit -m "Solve ABC003 A"
git push