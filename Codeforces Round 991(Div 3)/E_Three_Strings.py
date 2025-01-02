
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    def solve():
        a = input()
        b = input()
        c = input()

        n, m = len(a), len(b)
        dp = [[float('inf') for _ in range(m+1)] for _ in range(n + 1)]
        dp[n][m] = 0

        for left in range(n-1,-1,-1):
            dp[left][m] = dp[left+1][m]
            if a[left] != c[left+m]:
                dp[left][m] += 1

        for right in range(m-1,-1,-1):
            dp[n][right] = dp[n][right+1]
            if b[right] != c[right+n]:
                dp[n][right] += 1
        
        for left in range(n-1,-1,-1):
            for right in range(m-1,-1,-1):
                if a[left] != c[left+right]:
                    dp[left][right] = min(dp[left][right], 1+dp[left+1][right])
                else:
                    dp[left][right] = min(dp[left][right], dp[left+1][right])
                if b[right] != c[left + right]:
                    dp[left][right] = min(dp[left][right], 1+dp[left][right+1])
                else:
                    dp[left][right] = min(dp[left][right], dp[left][right+1])
        print(dp[0][0])

    t = int(input())
    for _ in range(t):
        solve()
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()


