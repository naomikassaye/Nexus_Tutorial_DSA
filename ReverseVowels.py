class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        n = len(s)
        s_list = list(s)
        start, end = 0, n - 1
        
        while start < end:
            while start < end and s_list[start] not in vowels:
                start += 1
            while start < end and s_list[end] not in vowels:
                end -= 1
            if start < end:
                s_list[start], s_list[end] = s_list[end], s_list[start]
                start += 1
                end -= 1
        
        return "".join(s_list)
