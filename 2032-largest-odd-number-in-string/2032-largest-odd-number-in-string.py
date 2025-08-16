class Solution:
    def largestOddNumber(self, num: str) -> str:
        # res=""
        # arr=int(num)
        # while arr > 0:
        #     a=arr%10
        #     if a %2==1:
        #         break
        #     arr//=10
        # return str(arr) if arr!=0 else ""
        s = str(num)
        for i in range(len(s)-1,-1,-1):
            if int(s[i]) % 2 == 1:
                return s[:i+1]
        return ""

        