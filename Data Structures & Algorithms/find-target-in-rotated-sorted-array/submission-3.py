class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for log n complexity need to do a binary search:

        #basic binary search
        '''
        nums = [0,1,2,3,4,5]
        l,r = 0 , (len(nums) -1) 
        middle = 0
        while l <= r:
            middle = int((r-l)/2)
            if nums[middle] < target:
                l = middle
            elif nums[middle] > target:
                r = middle
            else:
                return middle
        return -1
        '''

        list1 = nums[0:int(len(nums) * (2/3))]
        list2 = nums[int(len(nums) * (2/3)):len(nums)]

        if len(nums) == 3:
            list1 = nums[0:1]
            list2 = nums[1:4]


        print(list1)
        print(list2)
        l,r = 0 , (len(list1) -1) 
        middle = 0
        while l <= r:
            middle =  l + int((r-l)/2)
            if list1[middle] < target:
                l = middle + 1
            elif list1[middle] > target:
                r = middle - 1
            else:
                return middle

        l,r = 0 , (len(list2) -1) 
        middle = 0
        while l <= r:
            middle = l + int((r-l)/2)
            if list2[middle] < target:
                l = middle + 1
            elif list2[middle] > target:
                r = middle - 1
            else:
                return middle + len(list1)
        return -1


                


        