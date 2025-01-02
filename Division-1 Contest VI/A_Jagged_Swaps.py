def solve():
    n = int(input())
    nums = list(map(int,input().split()))
    if nums[0] != 1:
        return False
    return True

t = int(input())
for _ in range(t):
    if solve():
        print('YES')
    else:
        print('NO')