class Solution:
  def removeDuplicates(self, nums: [int]) -> int:
    for n in nums:
      if nums.count(n) > 1:
        while nums.count(n) > 1:
          nums.remove(n)
    print(nums)
    return len(nums)

s1 = Solution()
print(s1.removeDuplicates([1,1,1,1]))