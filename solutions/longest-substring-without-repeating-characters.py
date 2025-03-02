# Problem: Longest Substring Without Repeating Characters
# Difficulty: Unknown
# Solution:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_count = 0

        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[left])
                left += 1  
            char_set.add(s[i])  
            max_count = max(max_count, len(char_set))  

        return max_count
