def solve():
    p = input()
    s = input()
    left, right = 0, 0
    while left < len(p) and right < len(s):
        if p[left] != s[right]:
            return False
        cur_char = p[left]
        count_p = count_s = 0
        while left < len(p) and p[left] == cur_char:
            count_p += 1
            left += 1
        while right < len(s) and s[right] == cur_char:
            count_s += 1
            right += 1
        if count_p > count_s or count_s > 2*count_p:
            return False
    
    return left == len(p) and right == len(s)
t = int(input())
for _ in range(t):
    if solve():
        print("YES")
    else:
        print("NO")