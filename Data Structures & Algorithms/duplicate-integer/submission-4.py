class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = {}
        for i in nums:
            hashset[i] = 1 + hashset.get(i,0)
            if hashset.get(i,0) > 1:
                return True
        return False 
        