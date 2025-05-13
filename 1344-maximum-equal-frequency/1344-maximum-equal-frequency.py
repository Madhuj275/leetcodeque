from collections import Counter

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        dic = Counter(nums)
        dicdic = Counter(list(dic.values()))
        if len(nums) == 2:
            return 2
        
        while True:
            if len(dicdic) == 1 and (min(dicdic) == 1 or min(dicdic.values()) == 1):
                return len(nums)                
            if len(dicdic) == 2:
                max_dicdic_keys = max(dicdic)
                min_dicdic_keys = min(dicdic)
                if  max_dicdic_keys - min_dicdic_keys == 1 and dicdic[max_dicdic_keys] == 1:
                    return len(nums)
                if min_dicdic_keys == 1 and dicdic[min_dicdic_keys] == 1:
                    return len(nums)
            cleanup = nums.pop()
            if dic[cleanup] - 1 == 0:
                del dic[cleanup]
            else:
                dic[cleanup] = dic[cleanup] -1
            dicdic = Counter(list(dic.values()))
        
        return