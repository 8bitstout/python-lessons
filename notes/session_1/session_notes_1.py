'''
- what a program is
- basic syntax
- creating a program
- memory/compilers/interpreters
- webdev
  - JavaScript
  - CSS
  - HTML
  - Webservers
  - APIs
- backend
  - databases
  - Webservers
- comp sci
  - data structures
  - algorithms
'''
my_number = 5
my_other_number = 10

def add(a, b):
  return a + b

def add_and_print_without_returning(a, b):
  print("will not return")
  print(a + b)

my_sum = add(my_number, my_other_number)
print(my_sum)

add_and_print_without_returning(my_other_number, my_number)

my_string = "This is my string"

def say_hello(name):
  print("hello " + name)

my_name = "Justin"

say_hello(my_name)

'''

'''

'''
|  call add             | <- | a + b |
|  call next_add        |
'''
