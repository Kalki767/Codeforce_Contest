t = int(input())
for _ in range(t):
    n, k = [int(i) for i in input().split()]
    q = k // (n - 1)
    r = k % (n - 1)
    if k % (n - 1) == 0:
        print((n * q) - 1)
    else:
        print((n * q) + r)