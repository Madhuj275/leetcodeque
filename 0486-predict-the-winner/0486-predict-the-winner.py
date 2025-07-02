class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            dp[i] = nums[i]
            for j in range(i + 1, len(nums)):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        return dp[len(nums)-1] >= 0