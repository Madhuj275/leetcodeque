# Problem: 3Sum
# Difficulty: Unknown
# Solution:

class Solution:
    def threeSum(self, nums: List[int]) -> set:
        ans = set()
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                third = -(nums[i] + nums[j])
                if third in nums[j + 1:]:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    ans.add(tuple(temp))
        
        return list(ans)

