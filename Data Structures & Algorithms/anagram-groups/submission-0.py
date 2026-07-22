class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        output = []

        for i in range(len(strs)):
            temp = []    
            for j in range(len(strs)):
                if (self.checkAnagram(strs[i], strs[j])):
                    temp.append(strs[j])
            output.append(temp)
        
        # Sort inner lists and convert to tuples for set comparison
        seen = set()
        unique_data = []
        for group in output:
            sorted_group = tuple(sorted(group))
            if sorted_group not in seen:
                seen.add(sorted_group)
                unique_data.append(group)

        return unique_data
        
    def checkAnagram(self,s1,s2):
        charscount = {}

        for char in s1 :
            charscount[char] = charscount.get(char,0) + 1

        for char in s2 :
            charscount[char] = charscount.get(char,0) -1

        for value in charscount.values():
            if value !=0:
                return False

        return True
                
        