a = int(input())
b = int(input())
c = int(input())

print((a < b) + (a < c) + 1)
print((b < a) + (b < c) + 1)
print((c < a) + (c < b) + 1)