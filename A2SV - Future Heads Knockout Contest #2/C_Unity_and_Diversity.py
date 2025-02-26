red, blue = map(int,input().split())
petya, vasya = 0,0
cur_petya = 0
cur_vasya = 0
#choses red
cur_red, cur_blue = 1, 1
color = ['r','b']
while cur_red < red or cur_blue < blue:
    if color[-1] == 'b':
        if cur_blue < blue:
            color.append('b')
            cur_blue += 1
        else:
            color.append('r')
            cur_red += 1
    else:
        if cur_red < red:
            color.append('r')
            cur_red += 1
        else:
            color.append('b')
            cur_blue += 1
    if cur_red < red or cur_blue < blue:
        if color[-1] == 'b':
            if cur_red < red:
                color.append('r')
                cur_red += 1
            else:
                color.append('b')
                cur_blue += 1
        else:
            if cur_blue < blue:
                color.append('b')
                cur_blue += 1
            else:
                color.append('r')
                cur_red += 1
for i in range(1,red+blue):
    if color[i] == color[i-1]:
        cur_petya += 1
    else:
        cur_vasya += 1
if cur_petya >= petya:
    petya, vasya = cur_petya, cur_vasya

cur_petya = 0
cur_vasya = 0
#choses red
cur_red, cur_blue = 1, 1
color = ['b','r']
while cur_red < red or cur_blue < blue:
    if color[-1] == 'b':
        if cur_blue < blue:
            color.append('b')
            cur_blue += 1
        else:
            color.append('r')
            cur_red += 1
    else:
        if cur_red < red:
            color.append('r')
            cur_red += 1
        else:
            color.append('b')
            cur_blue += 1
    if cur_red < red or cur_blue < blue:
        if color[-1] == 'b':
            if cur_red < red:
                color.append('r')
                cur_red += 1
            else:
                color.append('b')
                cur_blue += 1
        else:
            if cur_blue < blue:
                color.append('b')
                cur_blue += 1
            else:
                color.append('r')
                cur_red += 1
for i in range(1,red+blue):
    if color[i] == color[i-1]:
        cur_petya += 1
    else:
        cur_vasya += 1
if cur_petya >= petya:
    petya, vasya = cur_petya, cur_vasya

print(petya, vasya)
