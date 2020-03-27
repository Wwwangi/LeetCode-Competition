# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=1
        right=n
        while left<=right:
            temp=(left+right)//2
            if isBadVersion(temp):
                right=temp-1
            else:
                left=temp+1
        return left

import bisect
class Solution():
    def firstBadVersion(self, n):
        class Wrap:
            def __getitem__(self, i):
                return isBadVersion(i)
        return bisect.bisect(Wrap(), False, 0, n)