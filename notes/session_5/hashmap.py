
# a dictionary in python is a hashmap. A hashmap is a data structure containing key/value pairs
# Every key in the hashmap is unique, so using the same key to add new data will overwrite
# an array with known unique indexes. The indexes are the key. The data at that index is the value.
# The key is created by using a hashing algorithm.

user: {
  'id': 1234,
  'name': 'Conor'
}

print(ord('a'))

class HashMap():
  def __init__(self):
    self.data = [1, 2, 3]

  def insert(self, key: str, val):
    h = self.get_key_hash(key)

    if h > len(self.data):
      for i in range(len(self.data), h):
        print(i)
        self.data.append(None)
      
      self.data.append(val)
    else:
      self.data[h] = val

  def get(self, key: str):
    return self.data[self.get_key_hash(key)]

  def get_key_hash(self, k: str) -> int:
    _hash = 0
    for char in k:
      _hash += ord(char)
    
    return _hash 

hashmap = HashMap()
hashmap.insert('justin', 'frick')

print(hashmap.get('justin'))
print(hashmap.data[669])
print(hashmap.data[hashmap.get_key_hash('justin')])

u = [0, 1]
u[0] = 1234
u[1] = 'Conor'

d = {
  0: 'a',
  1: 'b',
  2: 'c'
}

