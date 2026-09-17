A, op, B = input().split()
A = int(A)
B = int(B)

if op == "+":
    print(A + B)
elif op == '-':
    print(A - B)
elif op == '*':
    print(A * B)
elif op == '/' and B == 0:
    print('error')
elif op == '/':
    print(int(A / B))
elif op == '?' or '=' or '!':
    print('error')
