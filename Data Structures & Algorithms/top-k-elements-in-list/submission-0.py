import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #post watching video 
        freq = [[] for i in range(len(nums) + 1)]
        count = defaultdict(int)
        # value : count 
        for i in nums:
            count[i] = 1 + count.get(i,0)

        for number , frq in count.items():
            freq[frq].append(number)

        results = []

        for i in range( len(freq) - 1 , 0 , -1 ): # start, stop, step
            for j in freq[i]:
                results.append(j)
                if len(results) == k:
                    return results
                


'''        # array size of nums
        # index is count
        # value is lit of integers that map to that

        results = [[]] * len(nums)
        set_values = set(nums)
        print(set_values)
        for i in set_values:
            results[heap[i]].append(i)

        print(results)
        return []
        # pre watching videao 

        #heap questions - pop off heap k times
        # heapq.heapify is min-heap - need to negate values for max-heap

        results = []

        max_heap = [-i for i in nums]
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)
        for i in hashmap.values:
            
        for i in range(k):
            heapq.heapify(max_heap)
            results.append(-1* heapq.heappop(max_heap))

        return results   '''
