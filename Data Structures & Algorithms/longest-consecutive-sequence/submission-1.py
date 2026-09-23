class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        longest = 0

        for cur in nums:
            curlen = 0
            if cur - 1 not in hset:
                curlen += 1

                while cur + 1 in hset:
                    curlen += 1
                    cur = cur + 1

                longest = max(curlen, longest)
        return longest
