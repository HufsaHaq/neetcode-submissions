from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = defaultdict(int)
        for i in nums:
            seen[i] = 1 + seen.get(i,0)
            if seen[i] > 1:
                return True
        return False        