def solve():
    x, y, a, b = map(int,input().split())
    if (y-x) % (a+b) != 0:
        return -1
    return (y-x)//(a+b)

t = int(input())
for _ in range(t):
    print(solve())