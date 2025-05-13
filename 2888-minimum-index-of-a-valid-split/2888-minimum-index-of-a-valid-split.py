class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = {}
        max_count = 0
        dom = -1

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

            if count[num] > max_count:
                max_count = count[num]
                dom = num

        if max_count * 2 <= len(nums):
            return -1

        left_count = 0
        for i in range(len(nums)):
            if nums[i] == dom:
                left_count += 1

            len_left = i + 1
            len_right = len(nums) - len_left

            if 2 * left_count > len_left and 2 * (max_count - left_count) > len_right:
                return i

        return -1