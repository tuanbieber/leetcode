/*
 * @lc app=leetcode id=224 lang=cpp
 *
 * [224] Basic Calculator
 *
 * https://leetcode.com/problems/basic-calculator/description/
 *
 * algorithms
 * Hard (32.49%)
 * Total Accepted:    105.1K
 * Total Submissions: 323K
 * Testcase Example:  '"1 + 1"'
 *
 * Implement a basic calculator to evaluate a simple expression string.
 * 
 * The expression string may contain open ( and closing parentheses ), the plus
 * + or minus sign -, non-negative integers and empty spaces  .
 * 
 * Example 1:
 * 
 * 
 * Input: "1 + 1"
 * Output: 2
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: " 2-1 + 2 "
 * Output: 3
 * 
 * Example 3:
 * 
 * 
 * Input: "(1+(4+5+2)-3)+(6+8)"
 * Output: 23
 * Note:
 * 
 * 
 * You may assume that the given expression is always valid.
 * Do not use the eval built-in library function.
 * 
 * 
 */
class Solution {
public:
    int calculate(string s) {
        int res = 0, sign = 1, number = 0; 
        stack <int> st ; 

        for (auto &c: s) {
        	if (isdigit(c)) {
        		number = number * 10 + ((int) c - 48); 
        	} else if (c == '+') {
        		res += number * sign; 
        		number = 0; 
        		sign = 1; 
        	} else if (c == '-') {
        		res += number * sign;
        		number = 0; 
        		sign = -1; 
        	} else if (c == '(') {
        		st.push(res); 
        		st.push(sign); 
        		res = 0; 
        		sign = 1; 
        	} else if (c == ')') {
        		res += number * sign;
        		res *= st.top(); 
        		st.pop(); 
        		res += st.top(); 
        		st.pop(); 
        		number = 0; 
        	}
        }
        // say();
        return res + number * sign; 
    }
};



static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();
