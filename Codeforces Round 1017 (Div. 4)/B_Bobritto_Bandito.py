def solve():
    n, m, l, r = map(int, input().split())
    left, right = 0, 0
    if m > 0:
        mini = min(r - 0, m)
        right = mini
        m -= mini
    if m > 0:
        mini = min(0 - l,m)
        left = -mini
        m -= mini
    print(left, right)
t = int(input())
for _ in range(t):
    solve()