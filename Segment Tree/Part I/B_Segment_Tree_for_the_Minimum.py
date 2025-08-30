class SegmentTree :
    def __init__(self,n, default,arr):
        self.n = n
        self.arr = arr
        self.tree = [default for _ in range(2*self.n)]

        for index in range(n):
            self.tree[index+n] = self.arr[index]
        
        for index in range(n-1,0,-1):
            self.tree[index] = min(self.tree[index << 1] ,self.tree[index << 1 | 1])  
        
    def update(self,index,value):
        self.arr[index] = value

        index += self.n
        self.tree[index] = value

        while index > 1:
            self.tree[index >> 1] = min(self.tree[index] , self.tree[index ^ 1])
            index >>= 1
        
    def query(self,left,right):
        answer = float('inf')

        left += self.n
        right += self.n

        while left < right:
            if left & 1:
                answer = min(answer,self.tree[left])
                left += 1
            if right & 1:
                answer = min(answer,self.tree[right - 1])
                right -= 1
            
            left >>= 1
            right >>= 1
        
        return answer

n, m = map(int,input().split())
arr = list(map(int,input().split()))
tree = SegmentTree(n,float('inf'),arr)

for _ in range(m):
    op, first, second = map(int,input().split())
    if op == 1:
        tree.update(first,second)
    else:
        ans = tree.query(first,second)
        print(ans)