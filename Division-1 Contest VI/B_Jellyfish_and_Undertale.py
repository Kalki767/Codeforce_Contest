def solve():
    a, b, n = map(int,input().split())
    tools = list(map(int,input().split()))
    tools.sort(reverse= True)
    answer = 0
    for tool in tools:
        answer += (b - 1)
        b = 1
        b = min(tool + b, a)
    answer += b
    print(answer)

t = int(input())
for _ in range(t):
    solve()