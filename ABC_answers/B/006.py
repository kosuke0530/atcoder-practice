n = int(input())

a, b, c = 0, 0, 1

if n == 1:
    print(a)
elif n == 2:
    print(b)
elif n == 3:
    print(c)
else:
    for _ in range(n - 3):
        a, b, c = b, c, (a + b + c) % 10007

    print(c)