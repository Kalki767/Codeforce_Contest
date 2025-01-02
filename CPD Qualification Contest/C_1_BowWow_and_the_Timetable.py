import math


s = input()
if len(s) == 1:
    print(0)
else:
    length = len(s)
    departed = 0
    index = length - 1
    count_zeros = s.count('0')
    for i in range(index,0,-2):
        departed += 1
    
    if count_zeros < length - 1 and (length - 1) % 2 == 0:
        departed += 1
    print(departed)