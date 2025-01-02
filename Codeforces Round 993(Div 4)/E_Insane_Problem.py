import bisect

def solve():
    t = int(input())
    MAX_EXPONENT = 32  # Since 2^32 > 10^9
    
    for _ in range(t):
        k, l1, r1, l2, r2 = map(int, input().split())
        count = 0
        
        for n in range(MAX_EXPONENT + 1):  # Iterate over all powers n where k^n <= r2
            power = k ** n
            if power > r2:  # No point in proceeding if power exceeds r2
                break
            
            # Binary search for x: we need l1 <= x <= r1 and l2 <= x * power <= r2
            min_x = max(l1, (l2 + power - 1) // power)  # Ensure y = x * power >= l2
            max_x = min(r1, r2 // power)               # Ensure y = x * power <= r2
            
            if min_x <= max_x:  # Valid range
                count += (max_x - min_x + 1)
        
        print(count)

solve()
