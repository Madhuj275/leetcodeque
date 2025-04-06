class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  
        while n != 1:
            if n in seen:
                return False  
            seen.add(n)

            num = 0
            while n > 0:
                digit = n % 10
                num += digit * digit
                n //= 10
            n = num

        return True  