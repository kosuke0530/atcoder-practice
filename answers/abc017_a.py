a, x1 = map(int, input().split())
b, x2 = map(int, input().split())
c, x3 = map(int, input().split())

sa = a * x1 * 0.1
sb = b * x2 * 0.1
sc = c * x3 * 0.1
print(int(sa + sb + sc))