N = int(input())
T = [int(input()) for _ in range(N)]

Tnew = 100
for i in T:
    if i < Tnew:
        Tnew = i
        
print(Tnew)