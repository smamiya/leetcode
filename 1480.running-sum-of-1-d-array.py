#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
from typing import List
import itertools


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return itertools.accumulate(nums)
# @lc code=end

