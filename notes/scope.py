my_string = "this is a global string"

def print_global():
  local_string = "this is a local string"
  print(my_string)
  print(local_string)

  def print_local_string():
    cant_reach = "this wont be reached by print_global"
    print(local_string)
    print(cant_reach)
  
  print(cant_reach)
  print_local_string()

print_global()

'''
Recursion is calling the same thing over and over.
The key to recursion - a base case. A base case is the case
in which we can return from the recursion
'''

def factorial(n):
  if n == 1:
    return 1
  return n * factorial(n-1)

print(factorial(4))

'''
stack

first in last out aka FILO

| factorial(1)   | calls then pops returns 1
| factorial(2)   | calls then pops returns 2 * 1
| factorial(3)   | calls then pops returns 2 * 3
| factorial(4)   | calls then pops returns 6 * 4
'''

'''
Data Structures:
- Linked List
- Binary Tree
- Binary Search Tree
  - Red/Black Search Tree
  - B+ Tree
  - Log Sorted Merge Tree
- Graphs
- Stacks
- Queues
- Heaps
- Maps
'''

'''
# Binary Search Tree
[10, 2, 40, 20, 4, 5, 50, 25] # log(n) | n

        root - 10
        /  \
      2 .   40
       \ .  /
       4    20
'''


'''
Linked List
[1,2,3,4]
1 -> 2 -> 3 -> 4
Node
Property called next which contains the next node
functions: traverse, append, remove, reverse
'''

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None