# 3264. Final Array State After K Multiplication Operations I

class Solution(object):
  def getFinalState(self, nums, k, multiplier):
            """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
      for _ in range(k):
        # find minimum value and its index
        minValue = min(nums)
        minIndex = nums.index(minValue)

        # replace min value with new values
        nums[minIndex] = minValue * multiplier
      return nums
        
