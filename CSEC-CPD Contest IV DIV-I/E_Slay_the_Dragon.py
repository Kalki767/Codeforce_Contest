from bisect import bisect_left


def solve():
    n = int(input())
    strength = list(map(int,input().split()))
    strength.sort()
    m = int(input())
    total_sum = sum(strength)
    
    
    for _ in range(m):
        coins = 0
        defense, attack = map(int,input().split())
        index = bisect_left(strength, defense)

        if index == 0:
            coins += max(0, defense - strength[0])
            coins += max(0,attack - (total_sum - strength[0]))
            if index + 1 < 1:
                coins = min(coins, max(0, defense - strength[1]) + max(0, attack - (total_sum - strength[1])))
            
        else:
            coins = max(0, defense - strength[index-1]) + max(0, attack - (total_sum - strength[index-1]))
            if index < n:
                coins = min(coins, max(0, defense - strength[index]) + max(0, attack - (total_sum - strength[index])))
                
        
        print(coins)

solve()
