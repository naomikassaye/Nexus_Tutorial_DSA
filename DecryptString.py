class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans=[]
        n=len(s)
        i=0 

        while i<n:
            if i+2<n and s[i+2]=='#':
                num=s[i:i+2]
                i+=3
            else:
                num=s[i]
                i+=1
            ch=chr(int(num)+96)
            ans.append(ch)
            
        return ''.join(ans)
        
