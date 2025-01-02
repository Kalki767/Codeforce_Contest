import math


def solve():
    n = int(input())
    plan = list(map(int,input().split()))
    boxes = 0
    occupied = 0
    guniea_pigs = 0
    answer = 0
    for i in range(n):
        if plan[i] == 2:
            boxes_needed = (math.ceil((guniea_pigs-1)/2))
            if guniea_pigs:
                boxes_needed += 1
            occupied = boxes_needed
        else:
            if boxes - occupied > 0:
                occupied += 1
            else:
                boxes += 1
                occupied += 1
            answer = max(answer,boxes)
            guniea_pigs += 1
    answer = max(answer,boxes)
    print(answer)

t = int(input())
for _ in range(t):
    solve()