n = int(input())
chess = [['.' for _ in range(n)] for _ in range(n)]
row, col = 0,0
def inbound(row,col):
    return 0 <= row < n and 0 <= col < n
counter = 0
for col in range(0,n,2):
    r, c = row, col
    while inbound(r,c):
        counter += 1
        chess[r][c] = 'C'
        r += 1
        c += 1

row, col = 2, 0
for row in range(2,n,2):
    r, c = row, col
    while inbound(r,c):
        counter += 1
        chess[r][c] = 'C'
        r += 1
        c += 1
print(counter)
for r in range(n):
    current = ''.join(chess[r])
    print(current)