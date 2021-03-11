from collections import defaultdict

nums = [1,2,3,2,3,4]

names = {'conor': 'murphy'}

# remove the duplicate in O(n)
# For each number in the list,
# Check if that number is a key in the dictionary
# If it's not, then we haven't seen that number already
# Add it to the dictionary AND the new list
# If it IS in the list, do nothing because it's a duplicate (we've already visited it)
def deduplicate_list(arr: list) -> list:
  visited_nums = {}
  new_list = []

  for num in arr:
    s = f'Num: {num} | visited_nums before: {visited_nums}'
    if num not in visited_nums:
      visited_nums[num] = 'visited' # operation for dictionary
      new_list.append(num) # operation for list
    s += f' | visited_nums after: {visited_nums}'
    print(s)
  return new_list


print(nums)
print(deduplicate_list(nums))

d = {}

my_string = 'hello'

if (my_string == 'hello'):
  print("world")

try:
  my_string == 'world'
except:
  print("string is not world")

try:
  d['my key']
except:
  print("nope")

def default_behavior():
  print("key doesn't exist")

d = defaultdict(default_behavior)
d["my_key"]