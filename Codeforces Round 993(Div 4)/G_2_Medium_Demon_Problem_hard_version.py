from collections import deque


def solve():
    n = int(input())
    nums = list(map(int,input().split()))
    graph = [[] for _ in range(n)]
    in_degree = [0 for _ in range(n)]
    for index in range(n):
        reciever, donor = nums[index] - 1, index
        graph[donor].append(reciever)
        in_degree[reciever] += 1

   
    spiders = [1 for _ in range(n)]
    

    total_moves = 2
    queue = deque()
    for index in range(n):
        if in_degree[index] == 0:
            queue.append(index)
            
    
    while queue:
        
        node = queue.popleft()

        total_moves = max(total_moves, spiders[node] + 2)

        child = graph[node][0]

        spiders[child] += spiders[node]

        in_degree[child] -= 1
        if in_degree[child] == 0:

            queue.append(child)
        
             
    print(total_moves)
    


t = int(input())
for _ in range(t):
    solve()