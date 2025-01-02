def solve():
    number = list(input())
    n = len(number)

    for i in range(len(number)):
        
        cur_index, cur_max = i, int(number[i])
        ending = min(9,n - i)

        for j in range(ending):
            cur_value = int(number[i+j]) - j
            if cur_value > cur_max:
                cur_max = cur_value
                cur_index = i + j
        if cur_index != i:
            j = cur_index
            while j != i:
                number[j] = str(int(number[j]) - 1)
                number[j], number[j-1] = number[j-1], number[j]
                j -= 1
    return "".join(number)

t = int(input())
for _ in range(t):
    print(solve())