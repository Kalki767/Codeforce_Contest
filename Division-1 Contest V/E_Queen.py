n = int(input())
respect_parent = [1 for _ in range(n+1)]
respect_child = [1 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for i in range(n):
    parent, respect = map(int,input().split())
    if parent != -1:
        graph[parent].append(i+1)
    respect_parent[i+1] = respect_parent[i+1] and respect

for i in range(1,n+1):
    for child in graph[i]:
        respect_child[i] = respect_child[i] and respect_parent[child]
answer = []
for i in range(1,n+1):
    if respect_parent[i] and respect_child[i]:
        answer.append(i)
if answer:
    print(*answer)
else:
    print(-1)
        