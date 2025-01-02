from collections import defaultdict
import math


def solve():
    n = input()
    counter = defaultdict(int)
    total_sum = 0
    for i in range(len(n)):
        if n[i] == '2':
            counter[2] += 1
        elif n[i] == '3':
            counter[3] += 1
        total_sum += int(n[i])
    
    for i in range(counter[2]+1):
        if (total_sum + 2*i) % 3 == 0:
            if (total_sum + 2*i) % 9 == 0:
                return True
            if (total_sum + 2*i) % 9 == 3 and counter[3] >= 1:
                return True
            if (total_sum + 2*i) % 9 == 6 and counter[3] >= 2:
                return True
    return False
t = int(input())
for _ in range(t):
    if solve():
        print('YES')
    else:
        print('NO')