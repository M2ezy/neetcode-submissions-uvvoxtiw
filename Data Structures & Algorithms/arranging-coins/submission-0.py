class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 1
        coins = n
        while row <= coins:
            coins = coins - row
            row += 1
        return row - 1