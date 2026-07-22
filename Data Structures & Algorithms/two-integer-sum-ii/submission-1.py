class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) -1

        while l < r:
            sumcal = numbers[l] + numbers[r]

            if sumcal > target:
                r-=1
            elif sumcal < target:
                l+=1
            else:
                if l != r:
                    return [l + 1,r + 1]#The indices are 1-indexed (so the first element has index 1, not 0).
            
        return []
        