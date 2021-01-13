'''
Exercise: Write a function, sum_array, that takes an array as an argument and returns the sum of all integers in the array

Considerations: Can you write the function such that it terminates gracefully given an unexepected input such as an input that
is not an array or an array that contains elements that are not an integer?

Expectations: Test case should pass and print "Test case passed!"
'''

# Program -> your code goes below
def sum_array(arr):
    # solution goes here

# Tests
def test_sum_array(sum_array_function):
    arr = [1,2,3,4,5]
    solution = 15
    assert (sum_array_function(arr) == solution), f'Expected sum_array to return {solution} but instead returned {sum_array_function(arr)}'

test_sum_array(sum_array)

print("Test case passed!")
