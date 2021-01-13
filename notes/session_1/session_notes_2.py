'''
2 Datatypes

- Primitive data types
integers, floating point decimals, strings

'''
# Primitive datatypes are building blocks - you can add to them

my_int = 5
my_second_int = 3
my_float = 3.14

# None primitive datatypes
my_array = [1,1,1,1]
print(my_array)

# .            0         1         2         3

my_fruits = ["apple", "orange", "banana", "mango"]

print(my_fruits)

unique_fruits = set(my_fruits)

print(unique_fruits)


first_fruit = my_fruits[0]
print(first_fruit) # "apple"

last_fruit = my_fruits[3]
print(last_fruit) # "mango"

my_fruits_length = len(my_fruits)

print(my_fruits[my_fruits_length - 1])

# dictionary dict: map or a hashmap or a hashtable
# It stores key/value pairs

my_fruits = [ ["apple", "red"] , ["orange", "orange"], ["banana", "yellow"], ["mango", "burnt orange"], ["pear", "yellow"] ]

# we want to find mango and its color

for fruit_detail in my_fruits:
  fruit = fruit_detail[0]
  color = fruit_detail[1]
  print("Fruit is: "+ fruit)
  if fruit == "mango":
    print("{0} is the color {1}".format(fruit, color))

my_fruits = ["apple", "orange", "pear", "banana", "mango"]

def fruit_is_in_list(fruit_to_find):
  for fruit in my_fruits:
    if fruit == fruit_to_find:
      return True
  return False

fruit_to_find = "pear"
fruit_to_find = "pineapple"

print(fruit_to_find != "apple") # True

if fruit_is_in_list(fruit_to_find):
  print(fruit_to_find + " is in the list")
else:
  print(fruit_to_find +" is not in the list")

my_fruits = {
  "apple": "red",
  "pear": "yellow",
  "orange": "orange"
}

def get_fruit_color(fruit):
  return my_fruits[fruit]

print(get_fruit_color("apple"))

my_count = 0

for num in range(0,10):
  my_count += 1
  print(my_count)


