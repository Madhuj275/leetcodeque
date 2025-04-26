class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 0 or t < 0:
            return False
        
        from sortedcontainers import SortedDict
        
        sd = SortedDict()
        
        for i, x in enumerate(nums):
            if sd.bisect_right(x+t) - sd.bisect_left(x-t) > 0:
                return True
            if not x in sd:
                sd[x] = 0
            sd[x] += 1
            
            if len(sd) > k:
                y = nums[i-k]
                sd[y] -= 1
                if sd[y] == 0:
                    del sd[y]
                    
        return False