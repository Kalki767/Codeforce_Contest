from heapq import heapify, heappop, heappush


n, k = map(int,input().split())
nums = list(map(int,input().split()))
difference = []
cur_answer = nums[n-k] - nums[0]
for i in range(n-1,n-k,-1):
    difference.append(nums[i]-nums[i-1])

heapify(difference)
for i in range(n-k,0,-1):
    cur_diff = nums[i] - nums[i-1]
    heappush(difference,cur_diff)
    mini = heappop(difference)
    
    current = cur_answer - cur_diff + mini
    if current <= cur_answer:
        cur_answer = current

print(cur_answer)

