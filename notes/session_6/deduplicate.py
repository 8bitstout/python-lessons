nums = [1,2,3,2,3,4]

class Map:
  def __init__(self):
    self.data = {}
  
  def put(self, k, v):
    self.data[k] = v

  def get(self, k):
    if k in self.data:
      return self.data[k]
    return None

# remove the duplicate in O(n)
# For each number in the list,
# Check if that number is a key in the dictionary
# If it's not, then we haven't seen that number already
# Add it to the dictionary AND the new list
# If it IS in the list, do nothing because it's a duplicate (we've already visited it)
def deduplicate_list(arr: list) -> list:
  visited_nums = {}
  new_list = []

  for num in arr: #not length(arr)
    s = f'Num: {num} | visited_nums before: {visited_nums}'
    if num not in visited_nums:
      visited_nums[num] = 'visited' # operation for dictionary
      new_list.append(num) # operation for list
    else:
      print(f'{num} is already in the list')
    s += f' | visited_nums after: {visited_nums}'
    #print(s)
  return new_list

def deduplicate_list2(arr: list) -> list:
  visited_nums = Map()
  new_list = []

  for num in arr:
    s = f'Num: {num} | visited_nums before: {visited_nums.data}'
    if visited_nums.get(num) == None:
      visited_nums.put(num, 'visited') # operation for dictionary
      new_list.append(num) # operation for list
    s += f' | visited_nums after: {visited_nums.data}'
    print(s)
  return new_list

print(nums)
print(deduplicate_list(nums))

def printDuplicates(arr):
    dict = {}
 
    for ele in arr:
        try:
            dict[ele] += 1
        except:
            dict[ele] = 1
             
    for item in dict:
         
         # if frequency is more than 1
         # print the element
        if(dict[item] > 1):
            print(item, end=" ")
 
    print("\n")
 
# Driver Code
if __name__ == "__main__":
    list = [12, 11, 40, 12, 
            5, 6, 5, 12, 11]
    printDuplicates(list)