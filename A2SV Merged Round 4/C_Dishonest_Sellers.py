n, k = map(int,input().split())
current_week = list(map(int,input().split()))
after_discount = list(map(int,input().split()))
merged = list(zip(current_week,after_discount))
merged.sort()
ans = float('inf')
updated_current = [merged[i][0] for i in range(n)]
updated_after = [merged[i][1] for i in range(n)]
for i in range(1,n):
    updated_current += updated_current[i-1]
for i in range(n-1,-1,-1):
    updated_after += updated_after[i+1]
updated_after.append(0)
for i in range(k-1,n):
    cur = updated_current[i] + updated_after[k+1]
    ans = min(ans,cur)
merged.sort(key = lambda x : x[1])

