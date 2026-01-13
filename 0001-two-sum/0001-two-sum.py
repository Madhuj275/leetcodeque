class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        temp={}
        for i , num in enumerate(nums):
            c=target-num
            if c in temp:
                return [temp[c],i]
            temp[num]=i
        

        