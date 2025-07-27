class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        arr=[]
        arr.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                arr.append(nums[i])

        hill=0
        valley=0
        for i in range(1,len(arr)-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                hill+=1
            elif arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                valley+=1
        
        return hill+valley




            

        