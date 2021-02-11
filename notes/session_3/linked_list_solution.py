class Node():
  def __init__(self, data):
    self.data = data
    self.next = None

  def get_data(self):
    return self.data # returns 1

class Linked_List():
  def __init__(self):
    self.head = None

  def append(self, data):
    if not self.head:
      self.head = Node(data)
      return
    
    current_node = self.head
    while current_node.next is not None:
      current_node = current_node.next
    
    current_node.next = Node(data)
  
  def traverse(self):
    if not self.head:
      return

    current_node = self.head
    while current_node is not None:
      print(f'{current_node.data}')
      current_node = current_node.next

  
  # Visit every node in the list, and print the node's data/value
  def reverse(self):
    prev = None
    current_node = self.head
    while current_node is not None:
      nextnode = current_node.next
      current_node.next = prev
      prev = current_node
      current_node = nextnode
    self.head = prev


linked_list = Linked_List()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.traverse()