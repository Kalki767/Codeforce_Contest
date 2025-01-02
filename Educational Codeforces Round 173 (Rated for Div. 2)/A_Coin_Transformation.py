import math


def solve():
    n = int(input())
    ans = 0
    counter = 0
    while n > 3:
        counter += 1
        n//= 4
    return int(math.pow(2,counter))

t = int(input())
for _ in range(t):
    print(solve())