class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles) // 3
        final = 0
        
        for i in range(len(piles) - 2, n - 1, -2):
            final += piles[i]
        return final
