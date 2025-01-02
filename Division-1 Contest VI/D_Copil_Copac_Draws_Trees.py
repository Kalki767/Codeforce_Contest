def solve():
    n = int(input())
    edges = []
    readings = [-1 for _ in range(n)]
    for _ in range(n-1):
        u, v = map(int,input().split())
        u -= 1
        v -= 1
        u = min(u,v)
        v = max(u,v)
        if u != 0 :
            if readings[u] != 0 and readings[v] != 0:
                readings[u] = readings[v] = 1
        else:
            readings[u] = readings[v] = 0
        edges.append([u,v])
  
    edges.sort()
    for u, v in edges:
        readings[v] += readings[u]
    
    print(max(readings))

t = int(input())
for _ in range(t):
    solve()