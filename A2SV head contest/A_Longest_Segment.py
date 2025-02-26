n, k = map(int,input().split())
colors = list(map(int,input().split()))
ans = 1
counter = 1
for i in range(1,n):
    if colors[i] != colors[i-1]:
        counter += 1
    else:
        ans = max(ans,counter)
        counter = 1
ans = max(ans,counter)
print(ans)