n = int(input())
N = n / 1000

if N < 0.1:
    print("00")
elif 0.1 <= N <= 5:
    v = int(N * 10)
    print(f"{v:02d}")
elif 6 <= N <= 30:
    print(int(N + 50))
elif 35 <= N <= 70:
    print((int((N - 30) / 5) + 80))
elif 70 <= N:
    print(89)