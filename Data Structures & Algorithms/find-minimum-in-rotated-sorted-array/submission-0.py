class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums) -1
        minimum = float('inf')

        while l<= r:
            if nums[l] < nums[r]:
                if nums[l] < minimum: minimum = nums[l]
                break
            
            mid = (l + r)//2
            if nums[mid] < minimum: minimum = nums[mid]
                
            if nums[mid] >= nums[l]:
                    l = mid + 1
            else:
                    r = mid -1
                    

        return minimum
        