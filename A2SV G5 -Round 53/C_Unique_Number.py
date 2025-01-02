def solve():
    n = int(input())
    current = n
    if n <= 9:
        return n
    number = []
    starting = 9
    visited = set()
    total = 0
    while n > starting and starting > 0:
        number.append(str(starting))
        n -= starting
        total += starting
        visited.add(starting)
        starting -= 1
    if n > 0 and n not in visited and n <= 9:
        number.append(str(n))
        total += n
    if total == current:
        number.reverse()
        cur = int(''.join(number))
        return cur
    else:
        return -1
t = int(input())
for _ in range(t):
    print(solve())