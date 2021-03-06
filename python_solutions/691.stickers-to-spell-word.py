from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br
from functools import reduce
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=691 lang=python3
#
# [691] Stickers to Spell Word
#
# https://leetcode.com/problems/stickers-to-spell-word/description/
#
# algorithms
# Hard (40.72%)
# Total Accepted:    12.2K
# Total Submissions: 29.8K
# Testcase Example:  '["with","example","science"]\n"thehat"'
#
#
# We are given N different types of stickers.  Each sticker has a lowercase
# English word on it.
#
# You would like to spell out the given target string by cutting individual
# letters from your collection of stickers and rearranging them.
#
# You can use each sticker more than once if you want, and you have infinite
# quantities of each sticker.
#
# What is the minimum number of stickers that you need to spell out the
# target?  If the task is impossible, return -1.
#
#
# Example 1:
# Input:
# ["with", "example", "science"], "thehat"
#
#
# Output:
# 3
#
#
# Explanation:
# We can use 2 "with" stickers, and 1 "example" sticker.
# After cutting and rearrange the letters of those stickers, we can form the
# target "thehat".
# Also, this is the minimum number of stickers necessary to form the target
# string.
#
#
# Example 2:
# Input:
# ["notice", "possible"], "basicbasic"
#
#
# Output:
# -1
#
#
# Explanation:
# We can't form the target "basicbasic" from cutting letters from the given
# stickers.
#
#
# Note:
# stickers has length in the range [1, 50].
# stickers consists of lowercase English words (without apostrophes).
# target has length in the range [1, 15], and consists of lowercase English
# letters.
# In all test cases, all words were chosen randomly from the 1000 most common
# US English words, and the target was chosen as a concatenation of two random
# words.
# The time limit may be more challenging than usual.  It is expected that a 50
# sticker test case can be solved within 35ms on average.
#
#


class Solution:
    def minStickers(self, stickers, target):
        scc = [[0] * 26 for _ in range(len(stickers))]
        for i, s in enumerate(stickers):
            for c in s:
                scc[i][ord(c) - 97] += 1
        memo = {"": 0}

        def dp(curs):
            if curs in memo:
                return memo[curs]
            ans = 0x3f3f3f3f
            tar = Counter(curs)

            for i in range(len(scc)):
                # optimization
                if scc[i][ord(curs[0]) - 97] == 0:
                    continue

                nexts = ""
                for c in tar:
                    j = ord(c) - 97
                    if tar[c] > scc[i][j]:
                        nexts += c * (tar[c] - scc[i][j])

                ans = min(ans, 1 + dp(nexts))

            memo[curs] = ans # if ans < 0x3f3f3f3f else -1
            return memo[curs]

        x = dp(target)            
        return -1 if x >= 0x3f3f3f3f else x 


sol = Solution()
stickers, target = ["with", "example", "science"], "thehat"
stickers, target = ["notice", "possible"], "basicbasic"
print(sol.minStickers(stickers, target))
