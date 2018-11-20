# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.
# However, when you guess a particular number x,  and you guess wrong, you pay $x. You win the game when you guess the number I picked.
# Example:
# n = 10, I pick 8.
# First round:  You guess 5, I tell you that it's higher. You pay $5.
# Second round: You guess 7, I tell you that it's higher. You pay $7.
# Third round:  You guess 9, I tell you that it's lower. You pay $9.
# Game over. 8 is the number I picked.
# You end up paying $5 + $7 + $9 = $21.
# Given a particular n >= 1, find out how much money you need to have to guarantee a win.
# Credits:Special thanks to @agave and @StefanPochmann for adding this problem and creating all test cases.
#  https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/
require './aux.rb'

# @param {Integer} n
# @return {Integer}
def get_money_amount(n)
  v = Array.new(n + 1) { Array.new(n + 1, 0) }
  dp = lambda do |i, j|
    return 0 if i >= j
    return v[i][j] if v[i][j] != 0
    v[i][j] = ((i + j) / 2).upto(j).map { |k| [dp.call(i, k - 1), dp.call(k + 1, j)].max + k }.min
  end
  dp.call(1, n)
end

1.upto(10).each do |n|
  p [n, get_money_amount(n)]
end
