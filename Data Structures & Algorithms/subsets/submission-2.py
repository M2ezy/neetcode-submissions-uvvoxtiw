class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curres = []
        def dfs(i):
            if i == len(nums):
                res.append(curres.copy())
                return

            curres.append(nums[i])
            dfs(i + 1)

            curres.pop()
            dfs(i + 1)

        dfs(0)
        return res
        