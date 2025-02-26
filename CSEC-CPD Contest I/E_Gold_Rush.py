
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    def solve():
        n, m = list(map(int,input().split()))
        memo = {}
        def dp(number):
            first = second = False
            nonlocal m
            if number == m:
                return True
            
            if number % 3 != 0:
                return False
            
            x = number // 3
            y = 2 * x
            
            if x in memo:
                first = memo[x]
            else:
                first = dp(x)
                
                memo[x] = first
            if first:
                return first
            
            if y in memo:
                second = memo[y]
            else:
                second = dp(y)
                memo[y] = second
            if second:
                return second
            
            return False
        
        answer = dp(n)
        # print(memo)
        return answer

    t = int(input())
    for _ in range(t):
        if solve():
            print("YES")
        else:
            print("NO")
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
