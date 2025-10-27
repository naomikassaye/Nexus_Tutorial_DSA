class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store=set()
        longest=0
        l=0

        for r in range(len(s)):
            curr_char=s[r]
            while curr_char in store:
                store.remove(s[l])
                l+=1

            store.add(curr_char)
            longest=max(longest,r-l+1)

        return longest
    
        
