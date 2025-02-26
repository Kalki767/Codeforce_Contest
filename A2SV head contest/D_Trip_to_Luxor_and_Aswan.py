def solve():
    n, s = map(int,input().split())
    cost = list(map(int,input().split()))
    left, right = 0, n
    ans = 0
    total_cost = s

    def check(value):
        current_cost = []
        for i in range(n):
            current_cost.append(cost[i] + value * (i+1))
        current_cost.sort()
        return sum(current_cost[:value])
        
    while left <= right:
        mid = left + (right - left)//2
        total = check(mid)
        if total <= s:
            if  mid > ans:
                ans = mid
                total_cost = total
            elif mid == ans:
                total_cost = min(total_cost,total)
            left = mid + 1
        else:
            right = mid - 1
    print(ans,total_cost)
solve()