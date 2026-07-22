class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        values = []
        #changes what the values at index 0 is and basically doe sthe product on nums[1:last value]
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