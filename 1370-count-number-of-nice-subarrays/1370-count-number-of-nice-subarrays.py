class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res={0:1}
        curr=0
        count=0
        for num in nums:
            curr+=num%2
            if curr-k in res:
                count+=res[curr-k]
        
            res[curr]=res.get(curr,0)+1
        
        return count



        