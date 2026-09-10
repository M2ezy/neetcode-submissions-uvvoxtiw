class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        row = None
        while l <= r:
            mid = (r + l) // 2
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                row = matrix[mid]
                break
        if row is None:
            return False
        l = 0
        r = len(row)-1
        while l <= r:
            mid2 = (l + r) // 2
            if target > row[mid2]:
                l = mid2 + 1
            elif target < row[mid2]:
                r = mid2 - 1
            else:
                return True
        return False


