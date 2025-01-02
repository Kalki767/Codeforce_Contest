t = int(input())
for _ in range(t):
    m, a, b, c = map(int,input().split())
    first = 0
    if m >= a:
        first = a
    else:
        first = m
    if m >= b:
        second = b
    else:
        second = m
    remaining = (m-first) + (m-second)
    if remaining >= c:
        print(first + second + c)
    else:
        print(first + second + remaining)