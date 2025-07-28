class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        if n==0:
            return 0
        maxl=0
        maxr=0
        left=0
        right=n-1
        trapped=0
        while left <= right:
            if height[left] <=height[right]:
                if height[left]>=maxl:
                    maxl=height[left]
                else:
                    trapped+=maxl-height[left]
                left+=1
            else:
                if height[right]>=maxr:
                    maxr=height[right]
                else:
                    trapped+=maxr-height[right]
                right-=1
        return trapped