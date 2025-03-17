# Problem: Longest Valid Parentheses
# Difficulty: Unknown
# Solution:

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stack = [-1]
        ans = 0
        for i in range(n):
            c = s[i]
            if c == '(':
                stack.append(i)
                continue
            if len(stack) <= 1:
                stack = [i]
                continue

            stack.pop()
            ans = max(ans , i - stack[-1])
        return ans
            
            