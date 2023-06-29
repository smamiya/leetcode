#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       memo = []
       for num in nums:
            if num in memo:
                return True
            else:
                memo.append(num)

# @lc code=end

