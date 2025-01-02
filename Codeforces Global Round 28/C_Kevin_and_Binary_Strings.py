def solve():
    s = input()
    first_zero = -1
    for i in range(len(s)):
        if s[i] == '0':
            first_zero = i
            break
    length = len(s)
    answer = [1,length]
    if first_zero == -1:
        answer.extend([length, length])
    else:
        index = first_zero - 1
        right = first_zero + 1
        while index > -1 and right < length:
            if s[right] == '0':
                index -= 1
                right += 1
            else:
                break
        if index == -1:
            index = 0
        answer.extend([index + 1,index + (length - first_zero)])
    print(*answer)

t = int(input())
for _ in range(t):
    solve()