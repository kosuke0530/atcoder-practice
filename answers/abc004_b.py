a, b, c ,d = map(str, input().split())
e, f, g ,h = map(str, input().split())
i, j, k ,l = map(str, input().split())
m, n, o ,p = map(str, input().split())

print(p, o, n, m)
print(l, k, j, i)
print(h, g, f, e)
print(d, c, b, a)

"""
# 4行分のデータを2次元リストとして受け取る
grid = [input().split() for _ in range(4)]

# 行を逆順（下から上）、各行の要素も逆順（右から左）にして出力
for row in grid[::-1]:
    print(*row[::-1])
    
これらを駆使するともっとスマートに書ける
"""