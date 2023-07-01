#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hash = {}
        for i,email in enumerate(emails):
            localname = email[:email.find('@')]
            localname = localname.replace('.', '')
            if localname.find('+') > -1:
                localname = localname[:localname.find('+')]
            domainname = email[email.find('@'):]
            if  not localname + domainname in hash:
                hash[localname + domainname] = i
        return len(hash)
# @lc code=end

