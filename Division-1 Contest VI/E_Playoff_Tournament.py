class SegmentTree():
    def __init__(self,k,n,default):
        self.k = k
        self.n = n + 1
        self.tree = [default for _ in range(self.n)]

        for index in range(self.n//2):
            self.tree[index + self.n//2] = 2 if games[index + self.n//2 - 1] == '?' else 1
        
        for index in range(self.n//2 - 1, 0, -1):
            self.tree[index] = self.calculate(index,index << 1, index << 1 | 1)
        

    def calculate(self,index,left_child, right_child ):
        if games[index - 1] == '?':
            return self.tree[left_child] + self.tree[right_child]
        if games[index - 1] == '1':
            return self.tree[left_child]
        return self.tree[right_child]
     
    def update(self,index,value):
        games[index - 1] = value
        if index < self.n//2:
            self.tree[index] = self.calculate(index,index << 1,index << 1 | 1)
        
        else:
            self.tree[index] = 2 if games[index - 1] == '?' else 1
        
        while index > 1:
            if index & 1:
                self.tree[index >> 1] = self.calculate(index >> 1,index ^ 1,index)
            else:
                self.tree[index >> 1] = self.calculate(index >> 1,index,index ^ 1)
            index >>= 1

k = int(input())
games = list(input())
games.reverse()

n = len(games)
segment_tree = SegmentTree(k,n,0)
q = int(input())
for _ in range(q):
    index, value = input().split()
    index = n - int(index) + 1
    segment_tree.update(index,value)
    print(segment_tree.tree[1])
    
    
