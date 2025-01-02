def solve():
    n, p = map(int,input().split())
    spread = list(map(int,input().split()))
    cost = list(map(int,input().split()))
    spread_cost = list(zip(cost,spread))
    spread_cost.sort()
    counter = 1
    answer = p
    index = 0
    while counter < n:
        if spread_cost[index][0] < p:
            remaining = n - counter
            used = min(remaining,spread_cost[index][1])
            answer += (spread_cost[index][0] * used)
            index += 1
            counter += used
        else:
            answer += p
            counter += 1
    print(answer)

t = int(input())
for _ in range(t):
    solve()