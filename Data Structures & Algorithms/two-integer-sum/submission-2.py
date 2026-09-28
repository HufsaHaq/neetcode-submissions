from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)

        for index , value in enumerate(nums):
            desired = target - value
            if desired in hashmap.keys() and hashmap[desired] != index :
                return [hashmap[desired] , index]
            hashmap[value] = index
            
        