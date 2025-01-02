def solve():
    n = int(input())
    nums = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if nums[i] == 1:
            nums[i] += 1
            ans += 1
    for i in range(1,n):
        if nums[i] % nums[i-1] == 0:
            nums[i] += 1
            ans += 1
    print(*nums)
    
t = int(input())
for _ in range(t):
    solve()