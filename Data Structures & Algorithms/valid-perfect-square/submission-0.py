class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num
        while l<= r:
            middle = (l + r) // 2
            if middle * middle == num:
                return True
            if middle * middle < num:
                l = middle + 1
            else:
                r = middle - 1
        return False