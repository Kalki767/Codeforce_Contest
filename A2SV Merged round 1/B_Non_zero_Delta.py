n, a, b = map(int,input().split())
houses = [i for i in range(1,n+1)]
index = a - 1
if b < 0:
    houses.reverse()
    index = n - a
final_index = (index + abs(b))%n
print(houses[final_index])