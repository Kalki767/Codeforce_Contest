from bisect import bisect_left, bisect_right
from collections import defaultdict


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    count_bit = defaultdict(int)
    mx_length = nums[-1].bit_length()
    for num in nums:
        for i in range(mx_length):
            if num & (1 << i):
                count_bit[i] += 1
    count_bit = dict(sorted(count_bit.items() , reverse=True))
    print(count_bit)
    ans = 0
    for i in count_bit:
        if count_bit[i] <= n//2:
            ans = ans | (1 << i)
    
    diff = float('inf')
    cur = nums[0]
    for i in range(mx_length):
        if ans & (cur << i):
            diff += 2**(i)
    gain = 0
    for num in nums[1:]:
        cur_diff = 0
        cur_gain = 0
        length = num.bit_length()
        for i in range(length):
            num_setted = num & (1 << i)
            cur_setted = ans & (1 << i)
            if cur_setted:
                if not num_setted:
                    cur_diff += 2**(i)
            else:   
                if num_setted:
                    cur_gain += 2**(n - count_bit[i])
        if cur_diff < diff:
            cur = num
            diff = cur_diff
        elif cur_diff == diff:
            if cur_gain > gain:
                cur = num
                gain = cur_gain
    xor = 0
            
    for i in range(n):
        xor += (nums[i] ^ cur)

    print(xor)

t = int(input())
for _ in range(t):
    solve()