import numpy as np

A = list(map(int, input().split()))
mdn = np.median(A)
print(int(mdn))