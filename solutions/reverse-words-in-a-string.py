# Problem: Reverse Words in a String
# Difficulty: Unknown
# Solution:

class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        temp = ""
        ans = ""

        while left <= right:
            ch = s[left]
            if ch != ' ':
                temp += ch
            else:
                if temp != "":
                    if ans != "":
                        ans = temp + " " + ans
                    else:
                        ans = temp
                    temp = ""
            left += 1

        if temp != "":
            if ans != "":
                ans = temp + " " + ans
            else:
                ans = temp

        return ans

        
        