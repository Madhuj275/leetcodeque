class Solution:
    def triangleType(self, nums: List[int]) -> str:
        count=0
        nums.sort()
        seen=[]
        tsum=nums[0] + nums[1]
        if (tsum) <= nums[2]:
            return "none"
        for i in nums:
            if i in seen:
                count+=1
            else:
                seen.append(i)
        
        if count==2:
            return "equilateral"
        elif count==1:
            return "isosceles"
        else:
            return "scalene"


        