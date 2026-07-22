class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a hash map - if we have 1 then we are looking for 3 if the targety is 4
        hashmap = {}
        # cant use same element twice
        # key is the number - value is the indice
        for i in range(len(nums)):
            want = target - nums[i]
            if want in hashmap:
                return[hashmap[want],i]
            hashmap[nums[i]] = i

        return []

        