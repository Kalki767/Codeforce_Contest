n = int(input())
reversed = {'p':'q', 'q':'p','w':'w'}
for _ in range(n):
    s = list(input())
    ans = []
    s.reverse()
    for i in s:
        ans.append(reversed[i])
    print(''.join(ans))