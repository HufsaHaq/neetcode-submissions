class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        left , right = 0,len(nums)-1
        res = []
        print(nums)
    
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            while left <= right:
                print(nums[i])
                target = nums[i] + nums[left] + nums[right]
                if target == 0 and i != left != right:
                    res.append(sorted([nums[i],nums[left],nums[right]]))

                if target > 0:
                    right -= 1
                else:
                    left += 1

            left , right = 0,len(nums)-1

        seen = []

        for i in res:
            if i not in seen:
                seen.append(i)
        return seen


        