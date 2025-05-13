# Problem: Set Mismatch
# Difficulty: Unknown
# Solution:

class Solution:
    def findErrorNums(self, arr: list[int]) -> list[list[int]]:
        seen = set()
        duplicates = []
        for index, element in enumerate(arr):
            if element in seen:
                for dup in duplicates:
                    if dup[0] == element:
                        dup.append(index)
                        break
                else:
                    duplicates.append(element)
                    duplicates.append(index+1)
            else:
                seen.add(element)

        return duplicates


        