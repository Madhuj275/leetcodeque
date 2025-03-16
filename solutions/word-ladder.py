# Problem: Word Ladder
# Difficulty: Unknown
# Solution:

from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: set) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(endWord)
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            
            for i in range(len(word)):
                original_char = word[i]
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == original_char:
                        continue
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordList:
                        queue.append((new_word, steps + 1))
                        wordList.remove(new_word)
        
        return 0
