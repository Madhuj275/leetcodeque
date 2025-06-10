class Solution:
    def addBinary(self, a: str, b: str) -> str:

        maxx = max(len(a), len(b))
        a = a[::-1]
        b = b[::-1]
        
        carry = 0
        ans = []

        for i in range(maxx):

            bit_a = int(a[i]) if i < len(a) else 0
            bit_b = int(b[i]) if i < len(b) else 0
            
            temp = bit_a + bit_b + carry

            if temp == 0:
                ans.append('0')
                carry = 0
            elif temp == 1:
                ans.append('1')
                carry = 0
            elif temp == 2:
                ans.append('0')
                carry = 1
            elif temp == 3:
                ans.append('1')
                carry = 1
        
        if carry:
            ans.append('1')
            
        s = "".join(ans)


        return s[::-1]
        
        