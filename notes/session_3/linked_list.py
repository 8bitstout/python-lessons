fruit = {
  "name": 'apple',
  "color": 'red',
  "type": 'Granny Smith'
}

# Object Oriented Programming aka OOP -> Classes, extendability, abstract class are a template

class Person():
  # Constructor -> how we define a class
  # A method aka a function that belongs to a class
  # A class has properties. Every class of X type share
  def __init__(self, name):
    self.name = name

  def say_name(self):
    print(f'My name is, {self.name}')

  def say_hello_to(self, person):
    print(f'{self.name} says hello to {person.name}')

bob = Person("Bob")
alice = Person("Alice")

bob.say_name() # My name is, Bob
alice.say_name() # My name is, Alice

people = [bob, alice]

for person in people:
  person.say_name()

def say_hello_to(person_a, person_b):
  print(f'{person_a.name} says hello to {person_b.name}')

say_hello_to(bob, alice)

alice.say_hello_to(bob)

# "hashmap" <- key/value pairs

# Linked Lists
# Data structure that contains nodes which store a value and point to the next-most node
# 1 -> 2 -> 3 -> 4 -> None
# Node{data: 1} -> Node{data: 2} -> Node{data:3}
# It has a property, Head, which contains the first node in the list
# Methods:
#   1. Append
#   2. Traverse
#   3. Reverse 
#   4. Delete

'''
camelCase
PascalCase
snake_case
'''

class Node():
  def __init__(self, data):
    self.data = data
    self.next = None

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
    # Visit every node in the list, and print the node's data/value
  
  def reverse(self):
    # Reverse the linked list. 1 -> 2 -> 3 becomes 3 -> 2 -> 1
    # Mutate the current list rather than creating and returning a new list


linked_list = Linked_List()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

print(f'{linked_list.head.data} -> {linked_list.head.next.data} -> {linked_list.head.next.next.data}')