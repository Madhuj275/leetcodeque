class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)<=2:
            return list(set(nums))
        nums.sort()
        res=[]
        num1=0
        count1=0
        num2=0
        count2=0
        for i in nums:
            if i==num1 :
                count1+=1
                if count1 > len(nums)//3:
                    res.append(num1)
            elif i !=num1 and i == num2:
                count2+=1
                if count2 > len(nums)//3:
                    res.append(num2)
            elif i !=num1 and i !=num2:
                num1=i
                count1=1
            else:
                num2=i
                count2=1
        return list(set(res))
        
        

        

            
        