class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        arr=[]
        for i,val in enumerate(nums):
            for j in val:
                arr.append([j,i])
        k=len(nums)
        arr.sort()
        res=[-1e9,1e9]
        left=0
        n=len(arr)
        cntmp={}
        cnt=0
        for i in range(n):
            val,ind=arr[i]
            if(ind not in cntmp):
                cntmp[ind]=1
                cnt+=1
            else:
                cntmp[ind]+=1
            while(cnt==k):
                if(val-arr[left][0]<res[1]-res[0]):
                    res=[arr[left][0],val]
                cntmp[arr[left][1]]-=1
                if(cntmp[arr[left][1]]==0):
                    del cntmp[arr[left][1]]
                    cnt-=1
                left+=1
        return res