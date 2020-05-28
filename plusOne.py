class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    for i in range(len(digits)):
      if i + 1 == len(digits):
        digits[i] += 1

    while digits.count(10) > 0:
      j = digits.index(10)
      digits[j] = 0
      if j == 0:
        digits.insert(0, 1)
      else:
        digits[j - 1] += 1

    return digits