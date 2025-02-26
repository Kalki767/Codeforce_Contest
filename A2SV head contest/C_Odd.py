from collections import Counter
from heapq import heapify, heappop, heappush


def solve():
    n = int(input())
    nums = list(map(int,input().split()))
    counter = Counter(nums)
    nums = [-nums[i] for i in range(n) if nums[i]%2 == 0]
    
    nums = list(set(nums))
    heapify(nums)
    
    ans = 0
    while nums:
        cur = heappop(nums)
        ans += 1
        res = (-cur)//2
        if counter[res] > 0 or res % 2 != 0:
            continue
        counter[res] += 1
        heappush(nums,-res)
    print(ans)

t = int(input())
for _ in range(t):
    solve()