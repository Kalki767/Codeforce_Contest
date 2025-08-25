def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    flag = False
    ans = 0
    for i in range(n):
        if a[i] > b[i]:
            ans += a[i] - b[i]
        elif a[i] < b[i]:
            flag = True
    
    ans += 1 
    return ans

t = int(input())
for _ in range(t):
    print(solve())