def solve():
    n, x = map(int,input().split())
    first_different = -1
    if x == 0:
        answer = [0]*n
        return answer
    length = x.bit_length()
    for i in range(length):
        if (x >> i) % 2 == 0:
            first_different = 2**i
            break
    min_length = n-1 if first_different == -1 else min(first_different,n-1)
    answer = []
    res = 0
    flag = False
    for i in range(min_length):
        res |= i
        if res > x:
            flag = True
            break
        answer.append(i)

    remaining = n - len(answer)  
    if flag:
        answer.extend([x]*remaining)
        return answer

    
    if remaining == 1:
        if answer and (answer[-1] + 1) | res == x and (answer[-1] + 1) != first_different:
            answer.append(answer[-1]+1)
        else:
            answer.append(x)
    else:
        answer.extend([x]*remaining)
    return answer

t = int(input())
for _ in range(t):
    res = solve()
    print(*res)