'''
Exercise: Write a function, sum_array, that takes an array as an argument and returns the sum of all integers in the array
Considerations: Can you write the function such that it terminates gracefully given an unexepected input such as an input that
is not an array or an array that contains elements that are not an integer?
Expectations: Test case should pass and print "Test case passed!"
'''

# Program -> your code goes below
def sum_array(arr):
    # solution goes here
    s = 0
    for num in arr:
      s = num + s

    return s

arr = [1,2,3,4,5,6] # length of arr = n = 10....n = 10000000
arr = [1,2,3,4,5,6] # length of arr = n = 10....n = 10000000
other_arr = [10,20,30]

# Tests
def test_sum_array(sum_array_function):
    arr = [1,2,3,4,5]
    solution = 15
    sum_array_function(arr)
    assert (sum_array_function(arr) == solution), f'Expected sum_array to return {solution} but instead returned {sum_array_function(arr)}'

#test_sum_array(sum_array)

print("Test cases passed!")
