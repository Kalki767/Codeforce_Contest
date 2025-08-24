def solve():
    n = int(input())
    nums = list(map(int,input().split()))
    greater_numbers = [[0 for _ in range(n)] for _ in range(n)]
    lesser_numbers = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i+1,n):
            lesser_numbers[i][j] = lesser_numbers[i][j-1]
            greater_numbers[i][j] = greater_numbers[i][j-1]
            if nums[j] < nums[i]:
                lesser_numbers[i][j] += 1
            elif nums[j] > nums[i]:
                greater_numbers[i][j] += 1
    
    left = right = 1
    cur_difference = 0
    for i in range(n):
        for j in range(n):
            if lesser_numbers[i][j] - greater_numbers[i][j] > cur_difference:
                left, right = i+1, j+1
                cur_difference = lesser_numbers[i][j] - greater_numbers[i][j]
    
    print(left,right)

t = int(input())
for _ in range(t):
    solve()