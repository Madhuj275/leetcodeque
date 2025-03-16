# Problem: 3Sum Closest
# Difficulty: Unknown
# Solution:

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum=float('inf') 
        current=0
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left=i+1
            right=len(nums)-1
            while left < right:
                current=nums[i]+nums[left]+nums[right]
                if abs(current-target)  < abs(closest_sum-target):
                    closest_sum=current
                if(current < target):
                    left+=1
                # elif(current > target):
                #     right-=1
                else:
                    right-=1
        return closest_sum

