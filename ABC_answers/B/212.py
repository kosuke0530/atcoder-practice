A = str(input())
for i in A:
    if i != 0 and A[i - 1] == A[i]:
        continue
    