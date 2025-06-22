class Node(object):
  def __init__(self, has_end = False):
    self.has_end = has_end
    self.children = {}

class Trie(object):
  def __init__(self):
    self.head = Node(None)
  
  def insert(self, w):
    current_node = self.head
    
    for c in w:
      if c not in current_node.children:
        current_node.children[c] = Node()
      current_node = current_node.children[c]
        
    current_node.has_end = True

  def search(self, w):
    current_node = self.head
    for c in w:
      if c not in current_node.children:
        return False
      current_node = current_node.children[c]

    return current_node.has_end
  
  def starts_with(self, pref):
    current_node = self.head

    for c in pref:
      if c not in current_node.children:
        return False
      current_node = current_node.children[c]

    return True
  
  def delete(self, word):
    if not self.search(word):
      return False
    
    self._delete_helper(self.head, word, 0)
    
    return True
  
  def _delete_helper(self, node, word, idx):
    if idx == len(word):
      if node.has_end:
        node.has_end = False
      return len(node.children) == 0

    c = word[idx]

    if c in node.children:
      children_node = node.children[c]
      should_delete_child = self._delete_helper(children_node, word, idx + 1) 

      if should_delete_child:
        del node.children[c]
        return len(node.children) == 0 and not node.has_end

    return False
  