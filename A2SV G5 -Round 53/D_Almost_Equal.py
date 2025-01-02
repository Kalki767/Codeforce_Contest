n = int(input())
total = sum([i for i in range(1,2*n+1)])
if total % 2 == 0:
    print('NO')
else:
    half = total//2 + 1
    first_half = [2*n]
    second_half = [2*n-1]
    first, second = 2*n, 2*n - 1
    flag = True
    for i in range(n-1):
        if flag:
            first_half.append(first_half[-1]-3)
            flag = False
        else:
            first_half.append(first_half[-1]-1)
            flag = True
    flag = True
    for i in range(n-1):
        if flag:
            second_half.append(second_half[-1]-1)
            flag = False
        else:
            second_half.append(second_half[-1]-3)
            flag = True
    print('YES')
    first_half.extend(second_half)
    print(*first_half)