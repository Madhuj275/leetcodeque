class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res=set()
        for i in range(len(words)):
            for char in words[i]:
                if char==x:
                    res.add(i)
        
        return list(res)
            


        