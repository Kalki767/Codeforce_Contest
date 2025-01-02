def solve():
    n, k = map(int,input().split())
    nums = [i for i in range(1,n+1)]
    answer = []
    flag = True
    left, right = 0, n-1
    while left < right:
        if flag:
            cur = k - 1
            while left < right and cur > 0:
                answer.append(nums[right])
                right -= 1
                cur -= 1
            flag = False
        else:
            answer.append(nums[left])
            left += 1
            flag = True
    if left == right:
        answer.append(nums[left])
    print(*answer)
t = int(input())
for _ in range(t):
    solve()