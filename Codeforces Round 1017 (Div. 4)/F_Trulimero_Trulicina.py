def solve():
    n, m, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    
    def inbound(row,col):
        return 0 <= row < n and 0 <= col < m


    cur = 1
    for i in range(n):
        for j in range(m):
            if inbound(i-1,j):
                while graph[i-1][j] == cur:
                    cur += 1
            if inbound(i,j-1):
                while graph[i][j-1] == cur:
                    cur += 1
            graph[i][j] = cur
            cur += 1
            if cur > k:
                cur = 1

    for row in range(n):
        print(*graph[row])

t = int(input())
for _ in range(t):
    solve()