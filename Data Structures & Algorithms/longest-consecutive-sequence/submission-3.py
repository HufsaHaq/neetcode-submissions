class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set from list - this will be used to chcek neighbours
        numSet = set(nums)
        longest = 0 

        for n in nums:
            # finding the start of a sequence
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length +=1
                longest = max(length, longest)

    
        return longest

