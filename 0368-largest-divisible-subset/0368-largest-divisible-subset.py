class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = [[num] for num in nums]

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(ans[j]) + 1 > len(ans[i]):
                    ans[i] = ans[j] + [nums[i]]

        return max(ans, key=len)