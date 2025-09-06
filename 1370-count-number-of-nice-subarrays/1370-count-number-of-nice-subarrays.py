class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(nums,k):
            left=0
            n=len(nums)
            count=0
            odd=0
            for r in range(n):
                if nums[r]%2==1:
                    odd+=1
                while odd >k:
                    if nums[left]%2==1:
                        odd-=1
                    left+=1
                count += (r - left + 1)
                
            return count
        
        return helper(nums,k)-helper(nums,k-1)

        