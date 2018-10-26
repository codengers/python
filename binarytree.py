class Node:

  def __init__(self,key):

    self.left=None
    self.right=None
    self.val=key

root=Node(1)
root.left=2
root.right=3
root.left.left=Node(4)
print(root.val)
print(root.left)
print(root.right)
