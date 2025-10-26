
class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        count = Counter(nums)
        ans = 0
        for num in count:
            target = k - num
            if num == target:
                ans += count[num] // 2
            elif num < target:
                ans += min(count[num], count.get(target, 0))
        return ans
