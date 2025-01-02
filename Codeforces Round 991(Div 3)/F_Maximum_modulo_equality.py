import math


def solve():
    n, q = map(int,input().split())
    queries = []
   
    nums = list(map(int,input().split()))
    for _ in range(q):
        l, r = map(int,input().split())
        queries.append([l - 1,r-1])
    answer = []
    difference = []
    for i in range(1,n):
        difference.append(abs(nums[i]-nums[i-1]))
    n -= 1
    
    tree = [0 for _ in range(2*n)]
    for index in range(n):
        tree[index+n] = difference[index]

    for index in range(n-1,-1,-1):
        tree[index] = math.gcd(tree[index<<1],tree[index<<1 | 1])
    
    for l, r in queries:
        left, right = l + n, r + n
        result = 0
        while left < right:
            if left & 1:
                result = math.gcd(result, tree[left])
                left += 1
            if right & 1:
                right -= 1
                result = math.gcd(result, tree[right])
            left >>= 1
            right >>= 1
        answer.append(result)
    print(*answer)
    
    

t = int(input())
for _ in range(t):
    solve()
    

