'''
Exercise: Implement a basic calculator that supports add,subtract,multiply,divide
Basic requirements: four functions that perform the aforementioned operations will suffice.
Extending: Implement a function, calculator, that takes 3 inputs: operation (string), num_a, and num_b.
    the function, calculator, should perform the inputed operation as defined in the basic requirements and pass
    num_a and num_b to the respective function. I.e. if calculator is called with the arguments: "add", 5, 10
    then the add function should be called with 5 and 10 and return 15. If an operation is not recognized i.e "pow" return the
    following string: "Operation not recognized!".
Considerations: What happens if you try to divide by 0? Can you figure out a way to handle this case gracefully (without the programming crashing).
Expectations: All tests should pass. If all tests pass you should see your programm output: "All cases pass!"
Tests: the test functions should evaluate to True when called with the respective function
'''
# Program -> your code goes below

def addition(a,b): 
  return a + b 

def sub(a,b):
  return a - b

def multiply(a,b):
  return a * b

def divide(a,b):
  if b == 0:
    print("Divide by Zero Error")
    return
  return a/b

def calculator():
    #Input takes data as strings
    op = input('Which opertaion would you like to perform? : + - * / \n ')
    op = op.strip()
    print(op)

    input_is_valid = op == "*" or op == "/" or op == "+" or op == "-"

    while not input_is_valid:
      print(f'{op} is not a valid operation')
      op = input('Which opertaion would you like to perform? : + - * / \n ')
    
    num_a = float(input("enter first number"))

    num_b = float(input("enter second number"))

    if op == "+":
        my_sum = addition(num_a , num_b)
        print("{} + {} = ".format(num_a,num_b))
        print(my_sum)

    elif op == "-":
        my_sub = sub(num_a, num_b)
        print("{} - {} = ".format(num_a,num_b))
        print(my_sub)

    elif op == "*":
        my_multi = multiply(num_a, num_b)
        print("{} * {} = ".format(num_a,num_b))
        print(my_multi)

    elif op == "/":
        my_div = divide(num_a, num_b)
        print("{} / {} = ".format(num_a,num_b))
        print(my_div)

    else :
        print("Invalid selection")
# calculator()

# Tests
def test_add(add_function):
    expected_output = 15
    result = add_function(10,5)
    assert (result == expected_output), f'Add does not output the expected sum: 10 + 15 != {result}'

def test_subtract(subtract_function):
    expected_output = 5
    result = subtract_function(10,5)
    assert (result == expected_output), f'Subtract does not output the expected difference: 10 - 5 != {result}'

def test_multiply(multiply_function):
    expected_output = 50
    result = multiply_function(10, 5)
    assert (result == expected_output), f'Multiply does not output the expected product: 10 * 5 != {result}'

def test_divide(divide_function):
    expected_output = 2
    result = divide_function(10,5)
    assert (result == expected_output), f'Divide does not output the expected quotient: 10 / 5 != {result}'

# Add the name of your functions to the respective test arguments below
# I.e. if your add function is called add_nums, call the test like: test_add(add_nums)
# Note for clarification: It may be confusing to be passing a function name as a function parameter.
# This is valid in programming languages and it is called a first class function. When you define a function
# it's almost as if your assinging a block of code to that function namespace, like you would assign some data
# to a variable. So below we pass the name of the function, which is a reference, and we can execute that function
# when we call it with the normal syntax, using paren (), within our test functions.

test_add(addition)
test_subtract(sub)
test_multiply(multiply)
test_divide(divide)

print("All cases pass!")

calculator()