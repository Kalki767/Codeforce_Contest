def solve():
    n = int(input())
    nums = list(map(int,input().split()))
    answer = 0
    index = n-2
    while index >= 0:
        if nums[index] > nums[index+1]:
            answer += 1
            index -= 2
        else:
            index -= 1
    
    return answer

t = int(input())
for _ in range(t):
    print(solve())