class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set() # this is initializing the hashset
        for n in nums: # for every number in numbs
            if n in hset: #check if that number is already in our set
                return True # if it is return true
            hset.add(n) # if its not add it to our hset
        return False # if its not return false after checking every number in nums
        # this is o(n) time complexity as for checking if in hset is o(1) and checking for every number is o(n) so o(n) * o(1) = o(n) which is not constant but vary close
        
        