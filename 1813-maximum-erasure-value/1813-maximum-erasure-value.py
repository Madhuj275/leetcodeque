class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        seen=set()
        maxi=0
        tsum=0
        left=0
        for i in range(len(nums)):
            while nums[i] in seen:
                seen.remove(nums[left])
                tsum-=nums[left]
                left+=1
            seen.add(nums[i])
            tsum+=nums[i]
            maxi=max(maxi,tsum)
        
        return maxi


            


            

            



        