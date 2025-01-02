def solve():
    n = int(input())
    nums = list(map(int,input().split()))
    odd_sum = even_sum = 0
    odd_count = even_count = 0
    for i in range(n):
        if (i%2) == 0:
            even_sum += nums[i]
            even_count += 1
        else:
            odd_sum += nums[i]
            odd_count += 1
    odd_average, even_average = odd_sum//odd_count, even_sum//even_count
    if odd_sum%odd_count != 0 or even_sum%even_count != 0:
        return False
    if odd_average != even_average:
        return False
    return True

t = int(input())
for _ in range(t):
    if solve():
        print('YES')
    else:
        print('NO')