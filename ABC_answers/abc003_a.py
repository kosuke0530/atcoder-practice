n = int(input())
total = 0
x = 1
while n >= x:
    total += x *10000
    x += 1

print(total // n)