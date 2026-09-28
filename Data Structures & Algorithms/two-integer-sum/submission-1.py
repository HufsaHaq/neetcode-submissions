from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)

        for i in range(len(nums)):
            value = nums[i]
            desired = target - value
            if desired in hashmap.keys() and hashmap[desired] != i :
                return [hashmap[desired] , i]
            hashmap[value] = i
        return []
            

        