n, d = map(int,input().split())
cities = list(map(int,input().split()))
cities.sort()
opened = set()
ans = 0
for i in range(n):
    left_city, right_city = cities[i] - d, cities[i] + d
    if i != 0:
        if abs(left_city - cities[i-1]) >= d:
            opened.add(left_city)
    else:
        opened.add(left_city)
    if i < n - 1:
        if abs(right_city - cities[i+1]) >= d:
            opened.add(right_city)
    else:
        opened.add(right_city)

print(len(opened))