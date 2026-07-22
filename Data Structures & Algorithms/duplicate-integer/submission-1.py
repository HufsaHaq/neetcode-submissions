class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        compare = list(set(nums))
        compare.sort(reverse=True)
        print(compare)
        return not(nums == compare)
        