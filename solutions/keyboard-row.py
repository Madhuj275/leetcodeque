# Problem: Keyboard Row
# Difficulty: Unknown
# Solution:

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res=[]
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        for i in words:
            a=i.lower()
            if set(a).issubset(row1) or set(a).issubset(row2) or set(a).issubset(row3):
                res.append(i)
        return res
        