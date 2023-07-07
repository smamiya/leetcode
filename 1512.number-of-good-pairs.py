#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash = {}
        counter = 0
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:]):
                if num == num2:
                    counter += 1
        return counter
# @lc code=end

