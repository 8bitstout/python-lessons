# Binary Tree
# A Binary Tree has a few specfifc properties
# It contains 3 different types of nodes:
# 1. Root Node
# 2. Internal Node
# 3. Leaf Node

# The root node is the first node in the tree
# Every root and internal node has at least one child and at most 2 children
# These are usually referred to as the Left Child and Right Child
# If a node has no children, it is considered a leaf node - which means you're at the end of the tree

'''
                  5
                /   \
              2  3   8
             /      / \
            1 .    9 . 10
                        \
                         20
  
            unbalanced

            5
          /  \
         3    8
        /      \
       1        10

'''

[10, 5, 20, 4, 2, 30, 6]

'''
    10
   /  \
  5 .  20
 / \    \
 4 .6    30
 /
 2
'''


'''
BigO Notation

'''

# l = [1,2,] [5,8,9] [10,12,16,20,25]

# Bubble Sort n^2
# Time Sort
# Merge Sort logn

'''
    5
  /  \
 3    7
    

'''

# Find the duplicate number
l = [1,2,3,4,5,3,6,7,8]

for i in range(len(l)):
  first_num = l[i]
  for j in range(i, len(l)):
    if j+1 < len(l):
      second_num = l[j+1]
      if first_num == second_num:
        print(f"Found duplicate: {first_num} and {second_num}")


# Binary Search Tree (BST)
class Node():
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
  
class Binary_Search_Tree():
  def __init__(self):
    self.root = None
  
  def insert(self, data):
    if not self.root:
      self.root = Node(data)
      return
    
    self.insert_with_node(self.root, data)
  
  def insert_with_node(self, node, data):
    if data > node.data:
      if node.right is None:
        node.right = Node(data)
        return
      else:
        self.insert_with_node(node.right, data)
    
    if data < node.data:
      if node.left is None:
        node.left = Node(data)
        return
      else:
        self.insert_with_node(node.left, data)
  
  def traverse_in_order(self, node):
    if not node:
      return
    self.traverse_in_order(node.left)
    print(node.data)
    self.traverse_in_order(node.right)
  
  def is_in_bst(self, data_to_find):


bst = Binary_Search_Tree()
bst.insert(5)
bst.insert(10)
bst.insert(8)
bst.insert(12)

bst.insert(3)
bst.insert(4)
bst.insert(2)

print(bst.root.data) # 5
print(bst.root.right.data) # 10
print(bst.root.right.left.data) # 8
print(bst.root.right.right.data) # 12

print(bst.root.left.data) # 3
print(bst.root.left.right.data) # 4
print(bst.root.left.left.data) # 2
print("-------")
bst.traverse_in_order(bst.root)

'''
              5
            / . \
           3     10
         /  \   /  \
        2    4 8 .  12
'''