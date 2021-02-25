class Node():
    def __init__ (self, data):
        self.item = data
        self.left = None
        self.right = None

class Binary_Search_Tree():
    def __init__ (self):
        self.root = None

    def insert(self, data):
        if (self.root == None):
            self.root = Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self, data, curNode):
        if (data < curNode.item):
            if curNode.left == None:
                curNode.left = Node(data)
            else:
                self._insert(data,curNode.left)

        else:
            if curNode.right == None:
                curNode.right = Node(data)
            else:
                self._insert(data,curNode.right)
    
    def traverse_in_order(self,curNode):
        if curNode == None:
            return
        print(curNode.item)    
        self.traverse_in_order(curNode.left)
        self.traverse_in_order(curNode.right)
    
    def is_in_bst(self,data_to_find) -> bool:
        if self.root == None:
            return False
        else:
            return self._is_in_bst(self.root, data_to_find)
       
    '''
    def _is_in_bst(self, curNode, data_to_find):
        if curNode.item == None:
            return print('Not in tree')
        elif curNode.item == data_to_find:
            return print('Found data')
        else:
                if data_to_find < curNode.item:
                    return self._is_in_bst(curNode.left,data_to_find)
                else:
                    return self._is_in_bst(curNode.right,data_to_find)
    '''
    def _is_in_bst(self, curNode, data_to_find):
      if curNode == None:
        return False

      if curNode.item == data_to_find:
        return True
      
      if data_to_find < curNode.item:
        return self._is_in_bst(curNode.left,data_to_find)
      else:
        return self._is_in_bst(curNode.right,data_to_find)

'''
          10
        / .  \
      5  7      16
     /
    2
'''

#Driver Code
bst = Binary_Search_Tree()
bst.insert(5)
bst.insert(10)
bst.insert(8)
bst.insert(12)

bst.insert(3)
bst.insert(4)
bst.insert(2)

'''
print(bst.root.data)
print(bst.root.right.left.data)
'''

bst.traverse_in_order(bst.root)

bst.is_in_bst(8)
print(f'8 is in bst: {bst.is_in_bst(8)}')
print(f'11 is in bst: {bst.is_in_bst(11)}')

expected_values = [5, 10, 8, 12, 3, 4, 2]

#for val in expected_values:
  #assert(bst.is_in_bst(val) == True, f'Expected {val} to be in BST,')

# if __main__ == "main"

'''
# Project
- class a.py
- class b.py
- class c.py
- main.py
'''