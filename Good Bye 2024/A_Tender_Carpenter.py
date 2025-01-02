def solve():
    n = int(input())
    nums = list(map(int,input().split()))
    index = 1
    left = 0
    counter = 0
    while index < n:
        min_length = min(nums[left:index+1])
        max_length = max(nums[left:index+1])
        if (index - left) == 1:
            if sum(nums[left:index+1]) > max_length and min_length * 2 > max_length:
                left = index + 1
                counter += 1
                index += 2
            else:
                left += 1
                index += 1
    return counter > 0
t = int(input())
for _ in range(t):
    if solve():
        print('YES')
    else:
        print('NO')