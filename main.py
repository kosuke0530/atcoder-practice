N, D = map(int, input().split())
X = input().split()
ans = []
for i in range(N):
    for j in range(N + 1):
        j += 1
        if abs(X[i] - X[j]) < D:
            break
        
