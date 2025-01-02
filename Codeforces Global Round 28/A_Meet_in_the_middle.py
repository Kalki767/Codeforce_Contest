t = int(input())

for _ in range(t):
    x, y, a, b = [int(i) for i in input().split()]
    left = 0
    right =  x - y

    while left <= right:
        if left < right:
            left += a
            right -= b
        if left == right:
            print(left)
            break
        else:
            print(-1)
            break