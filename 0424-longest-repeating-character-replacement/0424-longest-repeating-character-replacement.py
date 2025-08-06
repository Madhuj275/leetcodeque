class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxi=0
        count=defaultdict(int)
        l=0
        temp=0
        for r in range(len(s)):
            count[s[r]]+=1
            temp= max(temp, count[s[r]])
            while (r-l+1) - temp >k:
                count[s[l]]-=1
                l+=1
            
            maxi=max(maxi,(r-l+1))
        return maxi



        