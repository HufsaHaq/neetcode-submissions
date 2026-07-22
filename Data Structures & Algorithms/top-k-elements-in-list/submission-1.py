from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(dict)
        for i in nums :
            count[i] = count.get(i,0) + 1
        #print(count)
        #print(count.keys())
        #print(count.values())
        minimum = 100004
        while len(count) != k:
            minimum = min(list(count.values()))
            temp = {k: v for k, v in count.items() if v > minimum} # keeps items in dict if they are bigger minimum
            count = temp

        return list(count.keys())