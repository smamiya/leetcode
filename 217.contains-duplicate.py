#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       hashmap = {}
       for i, num in enumerate(nums):
            if num in hashmap:
                return True
            else:
                hashmap[num] = i

# @lc code=end

