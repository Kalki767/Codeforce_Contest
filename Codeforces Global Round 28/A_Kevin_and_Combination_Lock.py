def solve():
    n = int(input())
    if n % 33 != 0:
        print('NO')
    else:
        print('YES')

t = int(input())
for _ in range(t):
    solve()