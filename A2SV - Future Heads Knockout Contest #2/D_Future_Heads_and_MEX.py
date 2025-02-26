from collections import Counter, defaultdict


def solve():
    n = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    counter = Counter(nums)
    counts = []
    unique = sorted(set(nums))
    for i in unique:
        counts.append(counter[i]-1)
    
    mini = float('inf')
    for i in range(len(unique)):
        if i != unique[i]:
            mini = i
            break
    if mini == float('inf'):
        mini = len(unique)
    graph = defaultdict(int)
    if mini < unique[0]:
        print(0)
    else:
        prev = [[0,-1]]
        
        graph[unique[0]] = -1
        for i in range(1,len(unique)):
            if mini < unique[i]:
                break
            cur = float('inf')
            previous = -1
            for j in range(i):
                if cur > counts[j]*unique[i] + prev[j][0]:
                    previous = unique[j]
                    cur = min(cur,counts[j]*unique[i] + prev[j][0])
            graph[unique[i]] = previous
            prev.append([cur,previous])
        cur_min = mini
        
        answer = float('inf')
        for i in range(len(prev)):
            node = unique[i]
            ans = 0
            cur_min = mini
            while node != -1:
                ans += (cur_min*(counter[node]-1) + node)
                cur_min = node
                node = graph[node]
            
            answer = min(answer,ans)
        print(answer)   
t = int(input())
for _ in range(t):
    solve()