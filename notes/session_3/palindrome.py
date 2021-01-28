# palindrome
# racecar
# toy problem

#len(word) = 7
#attempt 1
'''def is_palindrome(word: str) -> bool:
    for letter in range(0,len(word)):
        if word[letter] == word[(len(word)-1)]:
            return True
        else:
            return False

is_palindrome("racecar")'''

#attempt #2
def is_palindrome(word: str) -> bool:
    i =  0
    k = len(word)-1

    while i <= k:
      if word[i] != word[k]:
        return False
      i += 1
      k -= 1

    # If we make it through the whole string without finding unmatching chars, return True    
    return True


if is_palindrome('racecar'):
  # do something if True
        

word = 'racecfar'
print(len(word))
print(word[-3-1])

for i in range(0,len(word)):
    print(i)

#differnce between returning True and "True"?

def is_palindrome_2(word: str) -> bool:
    
    index = 0
    letter = 0

    while index < len(word) :
        index = 0
        letter = 0

        while word[index] == word[(-1 - index)] :
            index +=1
            letter +=1
            print(f'{word[letter]} and {word[index]}')
        return print('True')
            
    else :
            return print("False")
    

is_palindrome_2("racecar")


#kill %%


# test
def is_plaindrome_test(is_palindrome_fn):
  test_case = "racecar"
  test_case_false = "hello"
  assert(is_palindrome_fn(test_case) == True)
  assert(is_palindrome_fn(test_case_false) == False)