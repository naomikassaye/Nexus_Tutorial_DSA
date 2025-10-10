class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        cmn = Counter(words[0])
        for word in words[1:]:
            cmn &= Counter(word)  
        return list(cmn.elements())
