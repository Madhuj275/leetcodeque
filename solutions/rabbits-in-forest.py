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
            gsize=ans+1
            gcount=count[ans]
            num_grps=(gcount + gsize - 1) // gsize
            res += num_grps * gsize
        return res
            





        