# Data Types
In programming we deal with two different types of data:
1. Primitive data types
2. Non-Primitive data types

## Primitive Data Types
Primitive data types are the most basic data types. These are considered are building blocks of data.
They hold one single pure value of a type. In Python, these are strings, integers, floats, and booleans.
In lower level languages, we use a wider range of types such as signed and unsigned ints, signed and unsigned floats,
long ints, short ints, chars, bytes, bools, etc. The purpose of more precise types in lower level languages is to
manage the assignment of data more efficiently.

```python
# In Python we do not have to declare the type of data we are using, but the
# Python interpreter will processes data as intended

my_int = 5
my_float = 3.14
my_string = "hello"
my_bool = True

# Bools in Python are True and False
True == False # False
True == True # True
False == False # True

# Bools are binary - 1 & 0 where 1 is True and 0 is False
True == 1  # True
True == 0  # False
False == 0 # True
False == 1 # False

True + True   # 2
False + False # 0
```

In Python  we can freely perform operations between floats and ints.

```python
my_int = 5
my_float = 3.14

print(my_int + 3.14) # 8.14
print(my_float/my_int) # 0.628

# We can also remove decimal precision by using the // operator
# when we are dividing two integers that would result in a fraction

my_int = 10
my_other_int = 5
print(my_other_int//my_int) # 0

# However, the same operation using a decimal and integer would
# result in a float
print(my_float//my_int) # 0.0

# Also note that strings cannot be used with most  mathmetical operations in Python
# adding 4 to "word" would result in a raised exception
print(4+"word") # TypeError: can only concatenate str (not "int") to str

# We can, however, add two strings resulting in a concatenated string
str_a = "hello"
str_b = "world"

print (str_a + " " + str_b) # "hello world"

# We can also multiply strings
print(str_a * 3) # "hellohellohello"

# We can also "coerce" one type to another type using Python's provided functions
my_int = 5
my_float = float(my_int)
my_string = str(my_int)
my_int = my_int + int(my_string)

print(my_float) # 5.0
print(my_string) # "5"
print(my_int) # 10

# Strings can only be coerced given there is a valid int/flaot representation
a = "4"
b = "6"
print(int(a) + int(b)) # 10

my_string = "hello"
print(int(my_string) # ValueError: invalid literal for int() with base 10: 'hello'
```

## Non-Primitive Data Types
Non-Primitive data types store a collection of values.
In Python these are lists and dictionaries

## Lists
Lists are similar to arrays, but they are dynamic in the sense that they do not have a fixed length.
Python lists also have conveninate operatins. For example, we can add two lists together to
create a concatenated lists. We can dirctely access members of a list by using indexes.
Computers use 0 based indexes meaning that the first member of a list resides at index 0.
The last member of a list resides at n-1 where n is the length of the list. So if we have a
list of length 4 (4 members), we can access the first member using index 0 and the last
member using index 3.

```python
my_ints = [1,2,3,4]
my_colors = ["red", "green", "blue"]

# We use brackets to access members of the list
first_color = my_colors[0] # red
last_color = my_colors[3] # blue

# We can use the len() function provided by Python to get the length of a list
my_colors_length = len(my_colors) # 4
last_color = my_colors[my_colors_length - 1] # blue

# We can perform the operation inside the brackets as well
last_color = my_colors[len(my_colors) - 1] # blue
```

## Dictionaries
Dictionaries are a collection of key/value pairs where each key contains a value that will be returned.
You can access dictionaires using the same bracket notation as you would with a list. In the case of a
dictionary, instead of an index, we access the k/v pair using the key. A dictionary can hold any type of value.

```python
person = {
  "first_name": "Claude",
  "last_name": "Shannon",
  "dob": 1916,
  "books": ["A Mathematical Theory of Communication", "Communication Theory of Secrecy Systems", "Automata studies"]
}

# Note that keys in python are strings, so we must access the dict by providing the string representation of the key
print(person["first_name"]) # "Claude"
```
