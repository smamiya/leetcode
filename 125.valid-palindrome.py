#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
import re

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strList = list(re.sub('[^a-zA-Z0-9]+' ,'',s).lower())
        if len(strList) == 0:
            return True
        centerindex = len(strList) // 2
        for i in range(centerindex):
            if strList[i] != strList[-i-1]:
                return False
        return True
# @lc code=end

