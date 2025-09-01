class Solution(object):
    def subArrayRanges(self, nums):
        n = len(nums)
        temp = [(0,0,nums[0],nums[0])]  
        res = []

        while temp:
            l, r, cur_max, cur_min = temp.pop()
            if l < n and r < n:
                ran = cur_max - cur_min
                res.append(ran)

                if r+1 < n:
                    temp.append((l, r+1, max(cur_max, nums[r+1]), min(cur_min, nums[r+1])))

                if r == n-1 and l+1 < n:
                    temp.append((l+1, l+1, nums[l+1], nums[l+1]))

        return sum(res)
