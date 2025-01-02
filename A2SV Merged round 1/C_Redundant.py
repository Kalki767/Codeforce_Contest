s = input()
ans = 0
for i in range(len(s)): #100
    for j in range(i,len(s)): #100
        # print(s[i:j+1])
        if s[i:j+1] in s[i+1:]: #100
            ans = max(ans,j-i+1)
        else:
            break
print(ans)