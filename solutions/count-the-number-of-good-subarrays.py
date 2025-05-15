# Problem: Count the Number of Good Subarrays
# Difficulty: Unknown
# Solution:

class Solution:
    def countGood(self, nums, k):
        n = len(nums)
        counts = {}
        current = 0
        right = 0
        while right < n:
            num = nums[right]
            current += counts.get(num, 0)
            counts[num] = counts.get(num, 0) + 1
            if current >= k:
                break
            right += 1

        ans = 0
        left = 0
        while right < n:
            ans += n - right
            current -= counts[nums[left]] - 1
            counts[nums[left]] -= 1
            left += 1
            while current < k:
                right += 1
                if right == n:
                    break
                num = nums[right]
                current += counts.get(num, 0)
                counts[num] = counts.get(num, 0) + 1

        return ans