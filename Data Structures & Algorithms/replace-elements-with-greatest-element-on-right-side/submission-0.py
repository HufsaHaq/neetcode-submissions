class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]

        results = []

        left = 1
        right = len(arr)

        while left < right:
            results.append(max(arr[left:right:1]))
            left += 1
        results.append(-1)

        return results

        
        