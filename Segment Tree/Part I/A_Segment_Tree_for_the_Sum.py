class SegmentTree():
    def __init__(self,n,arr, default, func = max, ):
        self.tree = [default for _ in range(2*n)]
        self.n = n
        self.function = func

        #build the tree from the ground
        for index in range(n):
            self.tree[index + n] = arr[index]

        for index in range(n-1,-1,-1):
            self.tree[index] = self.function(self.tree[index << 1], self.tree[index << 1 | 1])

     
    def update(self,index,value):
        index += self.n
        self.tree[index] = value

        while index > 1:
            self.tree[index >> 1] = self.function(self.tree[index],self.tree[index ^ 1])
            index >>= 1
    
    def query(self,l,r):
        left, right = self.n + l, self.n + r

        result = 0
        while left < right:
            if left & 1:
                result = self.function(result,self.tree[left])
                left += 1
            
            if right & 1:
                right -= 1
                result = self.function(result, self.tree[right])
            
            left >>= 1
            right >>= 1
        
        return result


def add(a,b):
    return a+b 
n, m = map(int,input().split())
arr = list(map(int,input().split()))
segment_tree = SegmentTree(n,arr,0,add)
for _ in range(m):
    operation, u, v = map(int,input().split())
    if operation == 2:
        print(segment_tree.query(u,v))
    else:
        arr[u] = v
        segment_tree.update(u,v)
