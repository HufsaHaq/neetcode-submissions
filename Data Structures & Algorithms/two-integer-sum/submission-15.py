class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # have a hashset , if the value = traget exists then 2 sum works
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []