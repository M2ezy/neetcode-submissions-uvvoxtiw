class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 0
        l = 0
        r = n
        while l<= r:
            m = (l + r) // 2
            coins_needed = (m + 1) * (m / 2)
            if coins_needed > n:
                r = m - 1
            else:
                l = m + 1
                row = max(row, m)
        return row
            
