class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        left = {}
        right = {}

        for num in nums:
            if num in right:
                right[num] += 1
            else:
                right[num] = 1

        for i in range(len(nums)):
            if nums[i] in left:
                left[nums[i]] += 1
            else:
                left[nums[i]] = 1

            right[nums[i]] -= 1
            
            len_left = i + 1
            len_right = len(nums) - i - 1

            if 2 * left[nums[i]] > len_left and 2 * right.get(nums[i], 0) > len_right:
                return i

        return -1