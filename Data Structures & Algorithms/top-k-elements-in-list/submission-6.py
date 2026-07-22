class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap that has frequency as key and number as valuye
        '''
        key            value
        0
        1               1
        2               2,3
        3
        4
        len(nums)
        '''
        # so we traverse this hashmap from the bottem with teh biggest len/frequency and add 
        #that to res and stop when res >= k
        temp = {}
        for i in nums:
            temp[i] = 1 + temp.get(i,0)

        hash_map = defaultdict(list)
        for i in temp:
            hash_map[temp[i]].append(i)

        print(hash_map)

        res = []
        key = sorted(list(hash_map.keys()))
        print(key)
        for i in range(len(key) -1 ,-1, -1): #need to go to -1 and not 0 since we stop at 1 if we put 0
        #for i in range(len(key)):
            print(key[i])
            print(hash_map[key[i]])
            for i in hash_map[key[i]]:
                res.append(i)
            if len(res) >= k:
                break

        return res