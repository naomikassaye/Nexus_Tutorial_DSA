class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        right=int(math.sqrt(c))
        left=0

        while left<=right:
            current_sum = left * left + right * right
            if current_sum == c:
                return True
            elif current_sum < c:
                left += 1
            else:
                right -= 1
      
        return False

