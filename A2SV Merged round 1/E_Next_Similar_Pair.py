from collections import defaultdict, Counter

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():

   

    def dfs(v, p=-1):
        global ans
        bst = -1
        
        # Find the child with the largest subtree map
        for u in g[v]:
            if u != p:
                dfs(u, v)
                if bst == -1 or len(cnt[bst]) < len(cnt[u]):
                    bst = u

        # Merge smaller child maps into the largest one
        for u in g[v]:
            if u != p and u != bst:
                for x, y in cnt[u].items():
                    if x != a[v]:
                        ans += cnt[bst][x] * y
                    cnt[bst][x] += y

        # If there's a best child, swap its map with the current node's map
        if bst != -1:
            cnt[v], cnt[bst] = cnt[bst], cnt[v]
        
        # Update the answer and the count for the current node's value
        ans += cnt[v][a[v]]
        cnt[v][a[v]] = 1

    def solve():
        global n, a, g, cnt, ans
        
        # Input
        n = int(input())
        a = list(map(int, input().split()))
        g = [[] for _ in range(n)]
        
        for _ in range(n - 1):
            v, u = map(int, input().split())
            v -= 1
            u -= 1
            g[v].append(u)
            g[u].append(v)

        # Initialize global variables
        ans = 0
        cnt = [Counter() for _ in range(n)]
        
        # Run DFS
        dfs(0)
        
        # Output the result
        print(ans)
    t = int(input())
    for _ in range(t):
        solve()
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()



        