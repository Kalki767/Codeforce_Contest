from collections import Counter


def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    if len(nums) == 1:
        return False

    counter = Counter(nums)

    answer  = sorted(counter.values())
    

    index = 0
    while index < len(answer):
        if answer[index] <= 1:
            index += 1
            continue
        else:
            if index < len(answer) - 1 and answer[index] <= answer[index+1]:
                answer[index+1] -= answer[index]
            else:
                return False
        index += 1
    return True

t = int(input())
for _ in range(t):
    if solve():
        print('YES')
    else:
        print("NO")