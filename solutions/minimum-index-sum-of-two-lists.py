# Problem: Minimum Index Sum of Two Lists
# Difficulty: Unknown
# Solution:

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res=[]
        ans={}
        a=0
        for i in range(len(list1)):
            if list1[i] in list2:
                a= i + list2.index(list1[i])
                ans[list1[i]] = a
        if ans:
            min_a = min(ans.values())
            res.extend([key for key, value in ans.items() if value == min_a])
        return res
