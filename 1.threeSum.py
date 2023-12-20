class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    length = len(nums)

    for i in range(length - 2): # It stops at length - 2 because the subsequent code refers to elements at positions i, i + 1, and i + 2, so there should be at least three elements remaining
      # Skipping duplicate values
      if i > 0 and nums[i] == nums[i - 1]:
        continue

      l = i + 1
      r = length - 1

      while l<r:
        total = nums[i] + nums[l] + nums[r]

        if total < 0:
          l += 1
        elif total > 0:
          r -= 1
        else:
          res.append([nums[i], nums[l], nums[r]])
          while l < r and nums[l] == nums[l + 1]:
            l += 1
          while l < r and nums[r] == nums[r - 1]:
            r -= 1
          
          l += 1
          r -= 1

    return res