t = int(input())
for _ in range(t):
    x, y = [int(i) for i in input().split()]
    if y % x == 0:
        print(1,y//x)
    else:
        print(0,0)
