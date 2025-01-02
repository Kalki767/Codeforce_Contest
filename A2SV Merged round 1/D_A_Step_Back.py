import math


def solve():
    n, k, z = map(int,input().split())
    nums = list(map(int,input().split()))
    ans = 0
    prefix_sum = [nums[0]]
    for i in range(1,k+1):
        prefix_sum.append(prefix_sum[-1]+nums[i])
    
    length = len(prefix_sum)
    for i in range(1,length):
        moves_left = k - i
        left_move = min(z,math.ceil(moves_left/2))
        right_move = min(left_move, moves_left-left_move)
        remaining = moves_left - left_move - right_move
        current = prefix_sum[i] + left_move*nums[i-1] + (prefix_sum[i+remaining] - prefix_sum[i]) + right_move*(nums[i])
        ans = max(ans,current)
    
    print(ans)
t = int(input())
for _ in range(t):
    solve()