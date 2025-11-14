 class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        result = []
        j = 0
        m = len(spaces)
        n = len(s)
        
        for i in range(n):
            if j < m and i == spaces[j]:
                result.append(' ')
                j += 1
            result.append(s[i])
        
        return ''.join(result)
