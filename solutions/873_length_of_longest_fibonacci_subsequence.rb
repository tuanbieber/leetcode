# A sequence X_1, X_2, ..., X_nis fibonacci-like if:
#   n >= 3
#   X_i + X_{i+1} = X_{i+2}for alli + 2 <= n
# Given a strictly increasingarrayA of positive integers forming a sequence, find the length of the longest fibonacci-like subsequence of A. If one does not exist, return 0.
# (Recall that a subsequence is derived from another sequence A bydeleting any number ofelements (including none)from A, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)
#
# Example 1:
# Input: [1,2,3,4,5,6,7,8]
# Output: 5
# Explanation:
# The longest subsequence that is fibonacci-like: [1,2,3,5,8].
# Example 2:
# Input: [1,3,7,11,12,14,18]
# Output: 3
# Explanation:
# The longest subsequence that is fibonacci-like:
# [1,11,12], [3,11,14] or [7,11,18].
#
# Note:
#   3 <= A.length <= 1000
#   1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
#   (The time limit has been reduced by 50% for submissions in Java, C, and C++.)
#
#  https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/

# @param {Integer[]} a
# @return {Integer}
def len_longest_fib_subseq(a)
  return 0 if a.size < 3
  cache = a.zip(Array(0..a.size - 1)).to_h
  res = 0
  dp = Array.new(a.size) { Array.new(a.size, 2) }
  1.upto(a.size - 1).each do |i|
    (i + 1).upto(a.size - 1).each do |j|
      next unless cache.key?(a[j] - a[i])
      next if cache[a[j] - a[i]] >= i
      dp[i][j] = dp[cache[a[j] - a[i]]][i] + 1
      res = [res, dp[i][j]].max
    end
  end
  res > 2 ? res : 0
end

a = [1, 2, 3, 4, 5, 6, 7, 8]
#a = [1, 3, 7, 11, 12, 14, 18]
#a = [2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50]
p len_longest_fib_subseq(a)
