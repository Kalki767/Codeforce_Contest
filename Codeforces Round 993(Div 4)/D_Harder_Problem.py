from collections import defaultdict
import math


def solve():
    n = int(input())
    
    nums = list(map(int,input().split()))
    
    visited = set()
    start = 1
    ans = []
    for i in range(n):
        if nums[i] in visited:
            while start in visited:
                start += 1
            ans.append(start)
            visited.add(start)
            start += 1
        else:
            ans.append(nums[i])
            visited.add(nums[i])
    print(*ans)

t = int(input())
for _ in range(t):
    solve()