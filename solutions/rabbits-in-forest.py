# Problem: Rabbits in Forest
# Difficulty: Unknown
# Solution:

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        count = Counter(answers)
        res=0
        for ans in count:
            if ans > 0:
                res+=(ans+1)
            else:
                res+=(count[ans])
        
        return res
            





        