from collections import defaultdict 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        postfix = []
        current = 1
        results = []

        for i in range(len(nums)): # forwards
            prefix.append(current)
            current *= nums[i]
        #print(prefix)

        current = 1
        for i in range(len(nums) -1 , -1 , -1): # backwards
            postfix.append(current)
            current *= nums[i]

        #print(postfix)

        for i in range(len(nums)):
            temp = 1 
            #print(prefix[i])
            #print(postfix[len(prefix) - 1 - i])
            temp = prefix[i] * postfix[len(prefix) - 1 - i]
            results.append(temp)

        return results
        '''
        # using prefix
        current = 1
        results = []

        multiplication_map = defaultdict(int)
        order = []
        for i in range(len(nums) -1 , -1 , -1): # backwards
            order.append(nums[i])
            current *= nums[i]
            multiplication_map[tuple(order)] = current

        # pre fix = ( 0 * ...... * (i-1))   
        # suffix =  ( (i+1) * ..... * (len(nums) - 1) )
        
        order = []
        current = 1
        for i in range(len(nums)): # forwards
            order.append(nums[i])
            current *= nums[i]
            multiplication_map[tuple(order)] = current
        
        temp = 1
        for i in range(len(nums)):
            temp = 1 
            #temp =
        current = 1 multiplication_map.get(tuple(nums[:i]) , 1) * multiplication_map.get(tuple(nums[len(nums) - i : i : -1 ]) , 1) wrong heheheheheheh

            temp = multiplication_map.get(tuple(nums[:i]) , 1) * multiplication_map.get(tuple(nums[len(nums) - 1: i : -1 ]) , 1)
            results.append(temp)
            
            #0 1 2 3 4 
            #1 2 3 4 5

            #i = 3
            #1*2*3
            
            

        #print(multiplication_map)
        return results
'''
        # sliding window
        '''start = 1
        end = len(nums) - 1'''
        # issue is that it would O(n^2) solution since have to iterate over nums and also iter`ate over sliding window