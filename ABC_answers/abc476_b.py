N = int(input())
S = input()
T = input()

for i in range(N):
    if T[i] == '*':
        continue
    elif S[i] == T[i]:
        pass
    else:
        print('No')
        break
else:
    print('Yes')