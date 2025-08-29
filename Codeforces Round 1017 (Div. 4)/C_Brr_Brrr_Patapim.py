def solve():
    n = int(input())
    grid = []
    for _ in range(n):
        cur = list(map(int, input().split()))
        grid.append(cur)
    
    passcode = [0] * (2 *n)
    visited = set()
    for i in range(n):
        for j in range(n):
            passcode[i+j+1] = grid[i][j]
            visited.add(grid[i][j])
    
    for i in range(1,2*n+1):
        if i not in visited:
            passcode[0] = i
            break
    
    print(*passcode)

t = int(input())
for _ in range(t):
    solve()