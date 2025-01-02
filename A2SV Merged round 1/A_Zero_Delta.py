def solve():
    n, k = map(int,input().split())
    nums = list(map(int,input().split()))
    for i in range(n-1):
        if k == 0:
            break
        if nums[i] == 0:
            continue
        needed = min(nums[i],k)
        nums[i] -= needed
        nums[n-1] += needed
        k -= needed
    print(*nums)

t = int(input())
for _ in range(t):
    solve()