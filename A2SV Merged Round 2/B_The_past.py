n, k = map(int,input().split())
nums = list(map(int,input().split()))
lost = list(map(int,input().split()))
lost.sort(reverse = True)
left = 0
for right in range(n):
    if nums[right] == 0:
        nums[right] = lost[left]
        left += 1

if sorted(nums) == nums:
    print('No')
else:
    print('Yes')