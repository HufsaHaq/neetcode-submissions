class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hash set approach - we put things in one by one but befor putting it in we ask the hashmap if its alreafy in there
        hash_set = set({})  # doing just {} creates a dict and then cant use add func

        for i in  nums:
            if i in hash_set:
                return True
            else:
                hash_set.add(i)

        return False