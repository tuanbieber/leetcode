from collections import Counter, defaultdict
true = True
false = False
#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#
# https://leetcode.com/problems/next-greater-element-ii/description/
#
# algorithms
# Medium (53.20%)
# Total Accepted:    67.9K
# Total Submissions: 127.6K
# Testcase Example:  '[1,2,1]'
#
#
# Given a circular array (the next element of the last element is the first
# element of the array), print the Next Greater Number for every element. The
# Next Greater Number of a number x is the first greater number to its
# traversing-order next in the array, which means you could search circularly
# to find its next greater number. If it doesn't exist, output -1 for this
# number.
#
#
# Example 1:
#
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; The number 2 can't find
# next greater number; The second 1's next greater number needs to search
# circularly, which is also 2.
#
#
#
# Note:
# The length of given array won't exceed 10000.
#
#


class Solution:
    def nextGreaterElements(self, ns):
        sz = len(ns)
        if sz == 1:
            return [-1]
        ns = ns * 2
        res = [-1] * len(ns)
        q = []
        for i, n in enumerate(ns):
            while len(q) > 0 and q[-1][1] < n:
                j, m = q.pop()
                res[j] = n
            q.append((i, n))

        return res[:sz]


s = Solution()
ns = [1, 2, 5, 3, 1, 2, 6, 5, 4]
ns = [1, 2, 1]
print(s.nextGreaterElements(ns))
