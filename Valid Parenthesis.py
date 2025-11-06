class Solution:
    def isValid(self, s: str) -> bool:
      
        stack = []
        validpairs = {'()', '[]', '{}'}
      
        for char in s:
           
            if char in '({[':
                stack.append(char)
         
            else:
                
                if not stack or stack.pop() + char not in validpairs:
                    return False
      
        return not stack
