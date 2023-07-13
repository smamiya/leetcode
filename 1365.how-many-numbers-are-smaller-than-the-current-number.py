#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i,num in enumerate(nums):
            count = 0
            for num2 in nums:
                if num > num2:
                    count += 1
            result[i] = count
        return result
# @lc code=end

