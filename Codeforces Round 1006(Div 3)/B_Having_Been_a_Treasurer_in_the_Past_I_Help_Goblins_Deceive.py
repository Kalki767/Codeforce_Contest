import math


def solve():
    n = int(input())
    s = input()
    under_scores = scores = 0
    for i in s:
        if i == '_':
            under_scores += 1
        else:
            scores += 1
    
    left, right = math.ceil(scores/2), scores//2
    cur_value = right * under_scores
    answer = left * cur_value
    return answer

t = int(input())
for _ in range(t):
    print(solve())