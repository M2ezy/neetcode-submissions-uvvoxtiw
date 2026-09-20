class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r
        while l <= r:
            
            m = (l + r) // 2
            curLoad= 0
            days_needed = 1
            for weight in weights:
                if curLoad + weight <= m:
                    curLoad += weight
                else:
                    curLoad = weight
                    days_needed += 1
            if days_needed > days:
                l = m + 1
            else:
                r = m - 1
                res = min(res, m)
        return res  
                