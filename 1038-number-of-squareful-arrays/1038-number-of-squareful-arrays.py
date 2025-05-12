class Solution:
    def numSquarefulPerms(self, nums):
        self.count = 0

        def backtrack(ans,path):
            if not ans:
                self.count += 1 

            for i in range(len(ans)):
                if i and ans[i] == ans[i-1]:
                    continue 
                if not path or math.sqrt(path[-1]+ans[i]).is_integer():
                    backtrack(ans[:i]+ans[i+1:],path+[ans[i]])

        backtrack(sorted(nums),[])
        return self.count 