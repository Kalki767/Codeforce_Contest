n = int(input())
nums = list(map(int,input().split()))
sorted_nums = sorted(nums)
sorted_indexes = {}
indexes = {}

for index, num in enumerate(sorted_nums):
    sorted_indexes[num] = index

left = right = 0
stack = []
to_sit = sorted_nums[0]
next_index = 1
while right < n:
    if sorted_nums[right] == nums[right]:
        right += 1
        continue
    else:
        if right > 0:
            
