def solve():
    n = int(input())
    nums = list(map(int,input().split()))
    
    if n <= 2:
        return True
    left, right = nums[-2], nums[-1]

    counter = 0
    middle = float('inf')
    for i in range(n-3,-1,-1):
        if counter % 2 == 0:
            if nums[i] > left or nums[i] > right:
                return False
            middle = nums[i]
        else:
            if nums[i] > left or nums[i] > right:
                return False
            left, right = middle, nums[i]
        
        counter += 1
    
    return True

t = int(input())
for _ in range(t):
    if solve():
        print("YES")
    else:
        print("NO")
            