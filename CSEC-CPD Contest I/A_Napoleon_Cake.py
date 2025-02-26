def solve():
    n = int(input())
    creams = list(map(int,input().split()))
    answer = [0 for _ in range(n+1)]
    for i in range(n):
        if creams[i] == 0:
            continue
        left_index = max(0, i - creams[i] + 1)
        answer[left_index] += 1
        answer[i+1] -= 1
    
    for i in range(1,n+1):
        answer[i] += answer[i-1]

    for i in range(n):
        if answer[i] > 0:
            answer[i] = 1
    
    print(*answer[:-1])

t = int(input())
for _ in range(t):
    solve()