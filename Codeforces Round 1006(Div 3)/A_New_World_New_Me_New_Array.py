def solve():
    n, k, p = map(int,input().split())
    quotient = abs(k)//p
    remainder = abs(k) % p
    answer = quotient
    if remainder > 0:
        answer += 1
    if answer <= n:
        return answer
    return -1

t = int(input())
for _ in range(t):
    print(solve())