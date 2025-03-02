# Problem: Longest Substring Without Repeating Characters
# Difficulty: Unknown
# Solution:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_list=list(s)
        # left=0
        res=[]
        max_count=0
        for i in s_list:
            while i in res:  
                res.pop(0)
                # left += 1 
            
            res.append(i)
            max_count = max(max_count, len(res))
        
        return max_count
