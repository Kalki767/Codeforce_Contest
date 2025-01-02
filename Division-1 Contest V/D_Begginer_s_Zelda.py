import math


def solve():
    n = int(input())
    in_degree = [0 for _ in range(n+1)]
    for _ in range(n-1):
        u, v= map(int,input().split())
        in_degree[u] += 1
        in_degree[v] += 1
    leaf_nodes = 0
    for i in range(1,n+1):
        if in_degree[i] == 1:
            leaf_nodes += 1
    answer = math.ceil(leaf_nodes/2)
    print(answer)

t = int(input())
for _ in range(t):
    solve()