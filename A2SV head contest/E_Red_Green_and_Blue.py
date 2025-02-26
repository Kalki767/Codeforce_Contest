from bisect import bisect_left


def solve():
    n_green, n_blue, n_red = map(int,input().split())
    green = list(map(int,input().split()))
    blue = list(map(int,input().split()))
    red = list(map(int,input().split()))
    ans = float('inf')
    green.sort()
    blue.sort()
    red.sort()
    x, y, z = green[-1], blue[-1], red[-1]
    cur_x = cur_y = cur_z = float('inf')
    for i in range(n_green):
        cur_x = green[i]
        y_index = bisect_left(blue,cur_x)
        if y_index < n_blue:
            cur_y = blue[y_index]
            if y_index > 0 and abs(blue[y_index - 1] - cur_x ) < abs(cur_y - cur_x):
                cur_y = blue[y_index - 1]
            if y_index < n_blue-1 and abs(blue[y_index + 1] - cur_x ) < abs(cur_y - cur_x):
                cur_y = blue[y_index + 1]
        else:
            cur_y = blue[y_index-1]
        z_index = bisect_left(red,cur_x)
        if z_index < n_red:
            cur_z = red[z_index]
            if z_index > 0 and abs(red[z_index - 1] - cur_x ) < abs(cur_z - cur_x):
                cur_z = red[z_index - 1]
            if z_index < n_red - 1 and abs(red[z_index + 1] - cur_x ) < abs(cur_z - cur_x):
                cur_z = red[z_index + 1]
        else:
            cur_z = red[z_index-1]
        
        if (pow(cur_x - cur_y,2) + pow(cur_y - cur_z,2) + pow(cur_x - cur_z,2)) < (pow(x - y,2) + pow(x - z,2) + pow(y - z,2)):
            x, y, z = cur_x, cur_y, cur_z
    
    for i in range(n_blue):
        cur_x = blue[i]
        y_index = bisect_left(green,cur_x)
        if y_index < n_green:
            cur_y = green[y_index]
            if y_index > 0 and abs(green[y_index - 1] - cur_x ) < abs(cur_y - cur_x):
                cur_y = green[y_index - 1]
            if y_index < n_green-1 and abs(green[y_index + 1] - cur_x ) < abs(cur_y - cur_x):
                cur_y = green[y_index + 1]
        else:
            cur_y = green[y_index-1]
        z_index = bisect_left(red,cur_x)
        if z_index < n_red:
            cur_z = red[z_index]
            if z_index > 0 and abs(red[z_index - 1] - cur_x ) < abs(cur_z - cur_x):
                cur_z = red[z_index - 1]
            if z_index < n_red - 1 and abs(red[z_index + 1] - cur_x ) < abs(cur_z - cur_x):
                cur_z = red[z_index + 1]
        else:
            cur_z = red[z_index-1]
        
        if (pow(cur_x - cur_y,2) + pow(cur_y - cur_z,2) + pow(cur_x - cur_z,2)) < (pow(x - y,2) + pow(x - z,2) + pow(y - z,2)):
            x, y, z = cur_x, cur_y, cur_z 

    for i in range(n_red):
        cur_x = red[i]
        y_index = bisect_left(blue,cur_x)
        if y_index < n_blue:
            cur_y = blue[y_index]
            if y_index > 0 and abs(blue[y_index - 1] - cur_x ) < abs(cur_y - cur_x):
                cur_y = blue[y_index - 1]
            if y_index < n_blue-1 and abs(blue[y_index + 1] - cur_x ) < abs(cur_y - cur_x):
                cur_y = blue[y_index + 1]
        else:
            cur_y = blue[y_index-1]
        z_index = bisect_left(green,cur_x)
        if z_index < n_green:
            cur_z = green[z_index]
            if z_index > 0 and abs(green[z_index - 1] - cur_x ) < abs(cur_z - cur_x):
                cur_z = green[z_index - 1]
            if z_index < n_green - 1 and abs(green[z_index + 1] - cur_x ) < abs(cur_z - cur_x):
                cur_z = green[z_index + 1]
        else:
            cur_z = green[z_index-1]
        
        if (pow(cur_x - cur_y,2) + pow(cur_y - cur_z,2) + pow(cur_x - cur_z,2)) < (pow(x - y,2) + pow(x - z,2) + pow(y - z,2)):
            x, y, z = cur_x, cur_y, cur_z 
    first_diff = abs(x - y)
    second_diff = abs(x-z)
    thrid_diff = abs(y - z)
    answer = pow(first_diff,2) + pow(second_diff,2) + pow(thrid_diff,2)
    print(answer)

t = int(input())
for _ in range(t):
    solve()             