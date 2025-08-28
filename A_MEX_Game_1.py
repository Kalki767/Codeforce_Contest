from collections import Counter


def solve():
    n = int(input())
    nums = list(map(int,input().split()))
    counter = Counter(nums)
    nums_set = sorted(set(nums))
    mex = 0
    alice = True
    for i in range(len(nums_set)):
        if alice:
            if counter[mex] == 0:
                return mex
            alice = False
            
        else:
            if counter[mex] <= 1:
                return mex
            alice = True
        mex += 1

    return mex

t = int(input())
for _ in range(t):
    print(solve())