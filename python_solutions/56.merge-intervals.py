#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (35.48%)
# Total Accepted:    338.7K
# Total Submissions: 954.7K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:
# 
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    	intervals.sort(key=lambda x: x[0])
    	res = []
    	for i in intervals:
    		if len(res) == 0 or res[-1][1] < i[0]:
    			res.append(i)
    		else:
    			res[-1][1] = max(res[-1][1], i[1])
    	return res 



        
