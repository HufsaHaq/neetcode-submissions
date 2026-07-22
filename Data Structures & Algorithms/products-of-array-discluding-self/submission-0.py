class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        values = []
        for i in range(len(nums)):
            num = 1
            temp = nums[i]
            print(temp)
            nums.remove(temp)
            print(nums)
            nums.insert(0,temp)
            print(nums)
            for j in range(1, len(nums)):
                num *= nums[j]
            values.append(num)
        return values