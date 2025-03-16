# Problem: Relative Ranks
# Difficulty: Unknown
# Solution:

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_list = sorted(score, reverse=True)
        ranked_dict = {value: rank + 1 for rank, value in enumerate(sorted_list)}
        ranked_list = [ranked_dict[value] for value in score]
        for i in range(len(ranked_list)):
            if ranked_list[i]==1:
                ranked_list[i]="Gold Medal"
            elif ranked_list[i]==2:
                ranked_list[i]="Silver Medal"
            elif ranked_list[i]==3:
                ranked_list[i]="Bronze Medal"
            else:
                ranked_list[i]=str(ranked_list[i])
        return ranked_list