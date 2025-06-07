class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans =[]

        for i in range(len(nums)):
            while queue and nums[queue[-1]]<nums[i]:
                queue.pop()
            # always keep the max in the left 
            queue.append(i)
            # as index starts with 0 , if the window reaches i ( in fact has gone through i+1 elements ), we need let the left one go 
            if queue[0]+k == i: 
                queue.popleft()
            # do not add the max to the ans, until the widow reaches k 
            if i >=k-1:
                ans.append(nums[queue[0]])
        return ans 

            


        