N = int(input())
A = [int(x) for x in input().split()]

ans = 0
for i in range(N):
    if i == 0 or i % 2 == 0:
        ans += A[i]

print(ans)
