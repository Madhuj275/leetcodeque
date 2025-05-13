# Problem: Valid Parentheses
# Difficulty: Unknown
# Solution:

class Solution:
    def isValid(self, s: str) -> bool:
        def isValidHelper(s: str, index: int) -> bool:
            if index == len(s):
                return True
            
            if index + 1 < len(s) and s[index + 1] == ')':
                if s[index] == '(':
                    return isValidHelper(s, index + 2)
                else:
                    return False
            
            if index + 1 < len(s) and s[index + 1] == ']':
                if s[index] == '[':
                    return isValidHelper(s, index + 2)
                else:
                    return False
            
            if index + 1 < len(s) and s[index + 1] == '}':
                if s[index] == '{':
                    return isValidHelper(s, index + 2)
                else:
                    return False
            
            return isValidHelper(s, index + 1)

        return isValidHelper(s, 0)