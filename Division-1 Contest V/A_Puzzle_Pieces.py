def solve():
    n, m = map(int,input().split())
    if n == 1 or m == 1:
        return True
    if (n == 2) and (m == 2):
        return True
    return False

t = int(input())
for _ in range(t):
    if solve():
        print('YES')
    else:
        print('NO')