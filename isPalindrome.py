import re

def isPalindrome(s: str) -> bool:
  s = re.sub("[^a-zA-Z]+", "", s)
  left_i = 0
  right_i = len(s) - 1

  while left_i < right_i:
    if s[left_i].isalpha() != True:
      left_i += 1

    if s[right_i].isalpha() != True:
      right_i -= 1

    if s[left_i].lower() != s[right_i].lower():
      return False

    left_i += 1
    right_i -= 1

  return True

print(isPalindrome("A man, a plan, a canal: Panama"))