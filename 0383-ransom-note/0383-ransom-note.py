class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ans1=Counter(ransomNote)
        ans2=Counter(magazine)
        for char in ransomNote:
            if char in ans2:
                ans2[char]-=1
                # ans1[char]-=1
                if ans2[char]==0:
                    del ans2[char]
            else:
                return False
        
        return True