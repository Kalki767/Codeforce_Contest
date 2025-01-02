class SegmentTree():
    def __init__(self,n,arr, default, func = max, ):
        self.tree = [[float('inf'),0] for _ in range(2*n)]
        self.n = n
        self.function = func

        #build the tree from the ground
        for index in range(n):
            self.tree[index + n] = [arr[index],1]

        for index in range(n-1,-1,-1):
            self.tree[index] = self.combine(self.tree[index << 1], self.tree[index << 1 | 1])

    def combine(self,left,right):
        if left[0] < right[0]:
            return left
        if right[0] < left[0]:
            return right
        return [left[0], left[1] + right[1]] 
    
    def update(self,index,value):
        index += self.n
        self.tree[index] = [value, 1]

        while index > 1:
            self.tree[index >> 1] = self.combine(self.tree[index],self.tree[index ^ 1])
            index >>= 1
    
    def query(self,l,r,default):
        left, right = self.n + l, self.n + r

        result = [float('inf'),0]
        while left < right:
            if left & 1:
                result = self.combine(result,self.tree[left])
                left += 1
            
            if right & 1:
                right -= 1
                result = self.combine(result, self.tree[right])
            
            left >>= 1
            right >>= 1
        
        return result



n, m = map(int,input().split())
arr = list(map(int,input().split()))
segment_tree = SegmentTree(n,arr,float('inf'),min)
for _ in range(m):
    operation, u, v = map(int,input().split())
    if operation == 2:
        print(*(segment_tree.query(u,v,float('inf'))))
    else:
        arr[u] = v
        segment_tree.update(u,v)
