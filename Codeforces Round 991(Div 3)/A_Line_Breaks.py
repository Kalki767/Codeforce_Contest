def solve():
    n, m = map(int,input().split())
    ans = 0
    flag = True
    for _ in range(n):
        s = input()
        if flag and len(s) <= m:
            ans += 1
            m -= len(s)
        else:
            flag = False
    print(ans)

t = int(input())
for _ in range(t):
    solve()