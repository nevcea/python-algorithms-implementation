class Node:
  def __init__(self, v):
    self.v = v
    self.left = None
    self.right = None

class BST:
  def __init__(self, head):
    self.head = head
  
  def insert_node(self, v):
    self.base_node = self.head

    while True:
      if self.base_node.v > v:
        if self.base_node.left != None:
          self.base_node = self.base_node.left
        else:
          self.base_node.left = Node(v)
          break
      else:
        if self.base_node.right != None:
          self.base_node = self.base_node.right
        else:
          self.base_node.right = Node(v)
          break
  
  def search_node(self, v):
    self.base_node = self.head

    while self.base_node:
      if self.base_node.v == v:
        return True
      
      elif self.base_node.v > v:
        if self.base_node.left != None:
          self.base_node = self.base_node.left
        else:
          return False
        
      elif self.base_node.v < v:
        if self.base_node.right != None:
          self.base_node = self.base_node.right
        else:
          return False