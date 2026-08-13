class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i in range(len(nums)):
            hashset[nums[i]] = i

        for i in range(len(nums)):
            if (target - nums[i]) in hashset:
                index1 = i
                index2 = hashset.get(target - nums[i])
                if index1 != index2:
                    if index1> index2:
                        return [index2, index1]
                    else:
                        return [index1, index2]

        
        