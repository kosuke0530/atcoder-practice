N, M = map(int, input().split())
lst = [0] * N

while M > 0:
    for i in range(N):
        if M == 0:
            break
        lst[i] += 1
        M -= 1

for j in lst:
    print(j)
