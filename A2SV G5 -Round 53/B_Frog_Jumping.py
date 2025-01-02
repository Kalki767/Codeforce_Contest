import math


def solve():
    a, b, k = map(int,input().split())
    ans = a * (math.ceil(k/2)) - b* (k//2)
    print(ans)

t = int(input())
for _ in range(t):
    solve()