# Fizzbuzz
# print fizz if n is divisible by 3
# print buzz if n is divisible by 5
# print fizzbuzz if n is divisible by 3 and 5

def fizzbuzz():
  for num in range(1, 100):
    print(num)



def sum_array(arr):
    # solution goes here
    s = 0
    for num in arr:
      s = num + s

    return s

def sum_array2(arr):
  s = 0
  if (len(arr) == 0):
    return "array is empty, nothing to sum"

  index = 0
  
  while index < len(arr):
    s += arr[index]
    index += 1
  
  return s

def test_sum_array(sum_array_function):
  arr = [1,2,3,4,5]
  solution = 15
  sum_array_function(arr)
  assert (sum_array_function(arr) == solution), f'Expected sum_array to return {solution} but instead returned {sum_array_function(arr)}'

test_sum_array(sum_array2)

result = sum_array2([1,2,3,4,5])
print(result) # 15

  
'''
The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, starting with 0, and 1.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
'''

'''
4! = 1 * 2 * 3 * 4
'''

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
