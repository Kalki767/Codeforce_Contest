t = int(input())
for _ in range(t):
    sides = list(map(int,input().split()))
    sides.sort()
    ans = sides[0] * sides[2]
    print(ans)