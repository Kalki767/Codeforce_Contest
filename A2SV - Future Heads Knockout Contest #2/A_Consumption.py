n = int(input())
volume = list(map(int,input().split()))
capacity = list(map(int,input().split()))
total = sum(volume)
capacity.sort(reverse= True)
if total <= capacity[0] + capacity[1]:
    print('YES')
else:
    print('NO')