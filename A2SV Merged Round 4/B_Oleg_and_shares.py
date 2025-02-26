n, k = map(int,input().split())
numbers = list(map(int,input().split()))
def check():
    for i in range(n):
        if numbers[i] % k != 0:
            return False
    return True
if not check():
    print(-1)
else:
    mini = min(numbers)
    ans = 0
    for i in range(n):
        diff = numbers[i] - mini
        ans += (diff//k)
    print(ans)