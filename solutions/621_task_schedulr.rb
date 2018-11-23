# Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.
#
# However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.
#
# You need to return the least number of intervals the CPU will take to finish all the given tasks.
#
# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
# Note:
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].

# @param {Character[]} tasks
# @param {Integer} n
# @return {Integer}
def least_interval(tasks, n)
  gt = tasks.group_by(&:itself).values.sort_by(&:size).reverse
  m = gt[0].size
  k = gt.select { |g| g.size == m }.size
  [tasks.size, (n + 1) * (m - 1) + k].max
end

tasks = %w[A A A B B B C B]
tasks = %w[A A A B B B]
tasks = %w[a b a b]
tasks = %w[A A A B B B]
tasks = %w[A A A A A A B C D E F G]
n = 2
p least_interval(tasks, n)