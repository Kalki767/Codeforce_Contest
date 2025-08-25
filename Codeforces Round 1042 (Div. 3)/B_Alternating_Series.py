def solve():
    n = int(input())
    ans = []
    if n % 2 == 0:
        div = n//2 - 1
        ans.extend([-1,3]*div)
        ans.append(-1)
        if len(ans) < n:
            ans.append(2)
    else:
        div = n//2
        ans.extend([-1,3]*div)
        ans.append(-1)
    
    return ans
t = int(input())
for _ in range(t):
    print(*solve())