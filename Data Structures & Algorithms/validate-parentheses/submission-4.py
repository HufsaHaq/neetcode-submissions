class Solution:
    def isValid(self, s: str) -> bool:
        # stack approach
        # only append to stack if ( , [ or { then if you see a cling bracket it must be the same type of the opening bracket at the top of the stack
        # once they have been matched you can pop off that opening bracket from the stack
        stack = []

        hash_map = {'(' : ')',
                    '[' : ']',
                    '{' : '}'
                    }

        for i in s:
            if i in hash_map:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                current = stack[-1] #stack.peek() 
                if i == hash_map[current]:
                    stack.pop()
                else:
                    return False
                
        if len(stack) == 0:
            return True
        return False





        