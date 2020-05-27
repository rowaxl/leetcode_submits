from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
  # brute force pattern Time: O(n ** 2), Space: O(1)
  # for i in range(len(nums)):
  #   for j in range(i + 1, len(nums)):
  #     if nums[i] + nums[j] == target:
  #       return [i, j]

  # hash map pattern Time: O(n), Space: O(n)
  h = {}
  for i, num in enumerate(nums):
    print(f"i: {i}, num: {num}")
    n = target - num
    print(h)
    if n not in h:
      h[num] = i
    else:
      return [h[n], i]

print("answer: ", twoSum([3,2,4], 6))