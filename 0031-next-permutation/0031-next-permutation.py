class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]< nums[i+1]:
                idx=i
                break
        
        if idx==-1:
            nums.sort() 

        for i in range(len(nums)-1,idx-1,-1):
            if nums[i]> nums[idx]:
                nums[i],nums[idx]=nums[idx],nums[i]
                break
        
        nums[idx+1:] = sorted(nums[idx+1:])
        return nums
        

        
        