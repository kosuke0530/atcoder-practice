A = input()
B = input()
atcoder = "atcoder"
is_ok = True

for i in range(len(A)):
    a = A[i]
    b = B[i]
    if a == b:
        continue
    elif a == '@' and b in atcoder:
        continue
    elif b == '@' and a in atcoder:
        continue  
    else:
        is_ok = False
        break

if is_ok == True:
    print('You can win')
else:
    print('You will lose')

