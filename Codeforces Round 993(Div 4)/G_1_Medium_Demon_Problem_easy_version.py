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

    total_moves = 0
    queue = deque()
    for index in range(n):
        if in_degree[index] == 0:
            queue.append([index,0])
    
    while queue:
        
        length = len(queue)

        for _ in range(length):
            node, cur_move = queue.popleft()
            for child in graph[node]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append([child,cur_move+1])
        
        total_moves += 1

    print(total_moves + 2)
    
    


t = int(input())
for _ in range(t):
    solve()