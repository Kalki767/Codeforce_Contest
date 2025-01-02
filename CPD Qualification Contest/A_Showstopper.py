def solve():
    n = int(input())
    num1 = list(map(int,input().split()))
    num2 = list(map(int,input().split()))
    index = n-1
    while index > -1:
        if num1[index] > num2[index]:
            num1[index] , num2[index] = num2[index], num1[index]
        index -= 1
    return max(num1) == num1[-1] and max(num2) == num2[-1]

t = int(input())
for _ in range(t):
    if solve():
        print('Yes')
    else:
        print('No')