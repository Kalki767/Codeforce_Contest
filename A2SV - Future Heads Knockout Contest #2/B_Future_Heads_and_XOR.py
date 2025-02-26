a, c = map(int,input().split())
def convert(num):
    ans = []
    while num > 0:
        cur = num % 3
        ans.append(cur)
        num //= 3
    return ans
ter_a, ter_c = convert(a), convert(c)
max_length = max(len(ter_a),len(ter_c))
ter_a.extend([0]*(max_length - len(ter_a)))
ter_c.extend([0]*(max_length - len(ter_c)))
ter_b = []
for i in range(max_length):
    if ter_a[i] <= ter_c[i]:
        ans = int(ter_c[i]) - int(ter_a[i])
        ter_b.append(ans)
    else:
        if ter_c[i] == 1:
            ans = 4 - int(ter_a[i])
            ter_b.append(ans)
        elif ter_c[i] == 0:
            ans = 3 - int(ter_a[i])
            ter_b.append(ans)
        else:
            ans = 5 - int(ter_a[i])
            ter_b.append(ans)

answer = 0
for i in range(max_length):
    cur = pow(3,i) * ter_b[i]
  
    answer += cur
print(answer)