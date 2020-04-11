from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1404 lang=python3
#
# [1404] Number of Steps to Reduce a Number in Binary Representation to One
#
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/
#
# algorithms
# Medium (47.90%)
# Total Accepted:    8.6K
# Total Submissions: 17.8K
# Testcase Example:  '"1101"'
#
# Given a number s in their binary representation. Return the number of steps
# to reduce it to 1 under the following rules:
#
#
#
# If the current number is even, you have to divide it by 2.
#
#
# If the current number is odd, you have to add 1 to it.
#
#
#
# It's guaranteed that you can always reach to one for all testcases.
#
#
# Example 1:
#
#
# Input: s = "1101"
# Output: 6
# Explanation: "1101" corressponds to number 13 in their decimal
# representation.
# Step 1) 13 is odd, add 1 and obtain 14. 
# Step 2) 14 is even, divide by 2 and obtain 7.
# Step 3) 7 is odd, add 1 and obtain 8.
# Step 4) 8 is even, divide by 2 and obtain 4.
# Step 5) 4 is even, divide by 2 and obtain 2. 
# Step 6) 2 is even, divide by 2 and obtain 1.
#
#
# Example 2:
#
#
# Input: s = "10"
# Output: 1
# Explanation: "10" corressponds to number 2 in their decimal representation.
# Step 1) 2 is even, divide by 2 and obtain 1.
#
#
# Example 3:
#
#
# Input: s = "1"
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 500
# s consists of characters '0' or '1'
# s[0] == '1'
#
#
#


class Solution:
    def numSteps(self, s: str) -> int:
        res = carry = 0
        for i in range(len(s) - 1, 0, -1):
            res += 1
            if int(s[i]) + carry == 1:
                carry, res = 1, res + 1
        return carry + res


sol = Solution()
s = "1101"
# s = "1"
print(sol.numSteps(s))
