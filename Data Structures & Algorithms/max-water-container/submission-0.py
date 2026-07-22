class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lower_pointer = 0
        higher_pointer = len(heights) -1
        results = []
        while lower_pointer < len(heights) and higher_pointer > 0:
            print(f'lower_pointer {lower_pointer}')
            print(f'higher_pointer {higher_pointer}')
            print(f'heights[lower_pointer] {heights[lower_pointer]}')
            print(f'heights[higher_pointer] {heights[higher_pointer]}') 
            print(min([heights[lower_pointer],heights[higher_pointer]]) * abs(0 - lower_pointer + higher_pointer))         
            
            print(min([heights[lower_pointer],heights[higher_pointer]]))

            print(abs(0 - lower_pointer + higher_pointer))
            results.append(min([heights[lower_pointer],heights[higher_pointer]]) * abs(0 - lower_pointer + higher_pointer))
            if heights[lower_pointer] > heights[higher_pointer]:
                higher_pointer -= 1
            else:
                lower_pointer += 1

            # we move the pointer that has the smaller height value. 
            #because In the formula, the amount of water depends only on the minimum height. Therefore, it is appropriate to replace the smaller height value. 


        return max(results)


        