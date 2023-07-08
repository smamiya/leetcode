#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(nums[i])
            else:
                result.append(result[i-1] + nums[i])
        return result
# @lc code=end

