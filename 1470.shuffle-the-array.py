#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        lists1 = nums[:n]
        lists2 = nums[n:]
        for list1, list2 in zip(lists1, lists2):
            result.append(list1)
            result.append(list2)
        return result

# @lc code=end

