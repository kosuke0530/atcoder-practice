N, D = map(int, input().split())
X = int(input()).split()
ans = []

for i in range(N):
    for j in range(N + 1):
        j += 1
        if j == N:
            ans.append(X[i])
        if abs(X[i] - X[j]) < D:
            break

if not ans:
    print(0)
    print('')
else:
    print(len(ans))
    print(len)
        
        
# リタイア