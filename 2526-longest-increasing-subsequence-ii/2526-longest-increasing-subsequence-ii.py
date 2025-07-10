class Solution:
    def lengthOfLIS(self, nums, k):
        n = max(nums) + 1

        ans = [0]*(2*n) 

        def update(idx,val):
            idx += n
            ans[idx] = val

            while idx > 1:
                idx = idx//2
                ans[idx] = max(ans[2*idx],ans[2*idx+1])
        
        def getMax(left, right):
            left += n 
            right += n
            max_val = ans[left]

            while left < right:
                if left&1:
                    max_val = max(max_val,ans[left])
                    left += 1 
                if right&1:
                    right -= 1 
                    max_val = max(max_val,ans[right])
                left = left//2
                right = right//2
            
            return max_val

        for num in nums:
            prev_longest_sub = getMax(max(num-k,0),num)
            update(num,prev_longest_sub+1)

        return ans[1]