from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right 
from functools import reduce 
import string
true = True
false = False
#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#
# https://leetcode.com/problems/deepest-leaves-sum/description/
#
# algorithms
# Medium (87.89%)
# Total Accepted:    2.1K
# Total Submissions: 2.4K
# Testcase Example:  '[1,2,3,4,5,null,6,7,null,null,null,null,8]'
#
# Given a binary tree, return the sum of values of its deepest leaves.
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is between 1 and 10^4.
# The value of nodes is between 1 and 100.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        vs = []
        self.maxdepth = 0 
        def rec(node, depth):
            if not node: return 
            self.maxdepth = max(self.maxdepth, depth)
            vs.append((node.val, depth))
            rec(node.left, depth+1)
            rec(node.right, depth+1)
        rec(root, 0)
        return sum(v for v, d in vs if d == self.maxdepth)

sol = Solution()


