class Node:
  def __init__(self, v, height = 0, left = None, right = None):
    self.v = v
    self.left = left
    self.right = right
    self.height = height

class AVL:
  def __init__(self):
    self.root = None
  
  def height(self, base):
    if base is None:
      return 0
    return base.height

  def check_balance(self, base):
    if self.get_level_diff(base) < -1:
      if self.get_level_diff(base.right) > 0:
        base = self.relocate_right(base.right)
      base = self.relocate_left(base)

    elif self.get_level_diff(base) > 1:
      if self.get_level_diff(base.left) < 0:
        base = self.relocate_left(base.left)
      base = self.relocate_right(base)

    return base

  def get_level_diff(self, base):
    return self.height(base.left) - self.height(base.right)

  def relocate_right(self, base):
    next = base.left
    base.left = next.right
    next.right = base
    base.height = max(self.height(base.left), self.height(base.left)) + 1
    next.height = max(self.height(next.left), self.height(next.left)) + 1
    return next
  
  def relocate_left(self, base):
    next = base.right
    base.right = next.left
    next.left = base
    base.height = max(self.height(base.left), self.height(base.left)) + 1
    next.height = max(self.height(next.left), self.height(next.left)) + 1
    return next

  def recursion_put(self, base, v):
    if base is None:
      return Node(v, 1)
    if base.v < v:
      base.right = self.recursion_put(base.right, v)
    elif base.v > v:
      base.left = self.recursion_put(base.left, v)
        
    base.height = max(self.height(base.left), self.height(base.right)) + 1
    return self.check_balance(base)

  def put(self, v):
    if self.root is None:
      self.root = Node(v)
      return
    
    self.root = self.recursion_put(self.root, v)