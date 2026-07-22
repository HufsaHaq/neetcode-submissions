from collections import Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        nums = sorted(nums)
        temp = []
        starter = 0
        for j in nums:
            counter = 1
            if not((j-1) in nums):
                    starter = j
            else:
                continue
            for i in nums:
                if i == starter + 1:
                    counter +=1
                    starter += 1
            temp.append(counter)
        print(temp)
        return max(temp) if len(temp) > 0 else 0

    