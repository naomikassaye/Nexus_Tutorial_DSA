class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        nums_str.sort(key=lambda x: x*10, reverse=True)  
        res = ''.join(nums_str)
        return '0' if res[0] == '0' else res
