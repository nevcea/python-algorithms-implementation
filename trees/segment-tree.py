class SegmentTree:
  def __init__(self, arr):
    self.n = len(arr)
    self.tree = [0] * (2 * self.n)
    self.build(arr)
    
  def build(self, arr):
    for i in range(self.n):
      self.tree[self.n + i] = arr[i]
    
    for i in range(self.n - 1, 0, -1):
      self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
  
  def update(self, i, v):
    i += self.n
    self.tree[i] = v
  
    while i > 1:
      i //= 2
      self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

  def query(self, l, r):
    l += self.n
    r += self.n
    res = 0

    while l < r:
      if l % 2 == 1:
        res += self.tree[l]
        l += 1
      
      if r % 2 == 1:
        r -= 1
        res += self.tree[r]
      
      l //= 2

    return res