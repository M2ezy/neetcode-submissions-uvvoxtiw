class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Wil have a hashmap that stores every value, then will have an array that stores the values and its freq after will sort the freq from max and will will add to our ouput array until it reaches the len of k:

        res = {}
        for n in nums:
            res[n] = res.get(n, 0) + 1
        
        pairs = []
        for num, freq in res.items():
            pairs.append([num, freq])
        output = []
        pairs.sort(key=lambda x:x[1], reverse=True)
        for pair in pairs:
            output.append(pair[0])
            if len(output) == k:
                return output