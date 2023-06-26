#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
      
          """
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if (i != j) and (nums[i] + nums[j] == target):
                     return [i,j]

# @lc code=end

