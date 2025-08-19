class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() #-2,-1,0,0,1,2
        res=[]
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                left=j+1
                right=len(nums)-1
                if j > i+1 and nums[j]==nums[j-1]:
                    continue
                while left < right:
                    total = nums[i]+nums[j]+nums[left]+nums[right]
                    if total ==target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                    
                        while left < right and left > 0 and nums[left]==nums[left-1]:
                            left+=1
                        while left < right and right < len(nums)-1 and nums[right]==nums[right+1]:
                            right-=1

                    elif total < target:
                        left+=1
                    else:
                        right-=1
                
        return res
                    




        

        