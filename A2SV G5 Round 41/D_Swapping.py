def solve():
    n, x, m = map(int, input().split())
    left, right = x, x
    for _ in range(m):
        cur_left, cur_right = map(int, input().split())
        if cur_left > right or cur_right < left:
            continue
        left = min(left, cur_left)
        right = max(right, cur_right)
    print(right - left + 1)

t = int(input())
for _ in range(t):
    solve()