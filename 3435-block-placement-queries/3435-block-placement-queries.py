class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:

        obs=[]
        gaps=[inf]
        rolling_max=[inf]
        result=[]
        for q in queries:
            if q[0]==1:
                ind=bisect.bisect_left(obs,q[1])
                gap_splitted=gaps[ind]
                gaps[ind:ind+1]=[q[1]-(obs[ind-1] if ind>=1 else 0),(obs[ind] if ind != len(obs) else inf) -q[1]]
                rolling_max[ind:ind+1]=[None,None]
                for i in range(ind,len(rolling_max)):
                    old_val=rolling_max[i]
                    rolling_max[i]=max(rolling_max[i-1] if i>=1 else 0,gaps[i])
                    if i>=ind+2 and old_val==rolling_max[i]:
                        break
                bisect.insort_left(obs,q[1])

            elif q[0]==2:
                x=q[1]
                sz=q[2]
                ind=bisect_right(obs,x)
                #available_gaps=gaps[0:ind]
                max_available=max([rolling_max[ind-1] if ind>=1 else 0]+[x-(obs[ind-1] if ind>=1 else 0)])
                result.append(max_available>=sz)
        return result