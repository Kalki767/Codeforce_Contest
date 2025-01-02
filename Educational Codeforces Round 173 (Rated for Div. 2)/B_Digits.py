def solve():
    n, d = map(int,input().split())
    ans = set()
    odds = [1,3,5,7,9]
    if n >= 6:
        ans = set([1,3,7])
        if n < 9:
            if d% 2 != 0:
                ans.add(9)
        else:
            ans.add(9)
        if d == 5:
            ans.add(5)
        ans = list(ans)
        ans.sort()
    elif n >= 3:
        ans = set([1,3,7])
        if d == 5:
            ans.add(5)
        ans = list(ans)
        ans.sort()
    else:
        number = int(str(d) * n)
        for odd in odds:
            if number % odd == 0:
                ans.add(odd)
        ans = list(ans)
        ans.sort()
    print(*ans)

t = int(input())
for _ in range(t):
    solve()