Q = int(input())
S = input()
T = input()

for i in range(Q):
    q1, q2 = map(int, input().split())
    cw = S[q1 - 1:q2]
    if S[-(len(T)):] == cw or S[:len(T)] == cw:
        print('YES')
    else:
        print('NO')
        
        # リタイア