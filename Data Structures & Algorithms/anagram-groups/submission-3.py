from collections import Counter 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we make key a hash set and group hashsets?
        hashset = {}
        
        for i in range(len(strs)):
            temp = {}
            for j in range(len(strs[i])):
                temp[strs[i][j]] = 1 + temp.get(strs[i][j],0)

            c = Counter(temp)
            key = tuple(sorted(c.items())) # dict cant take dict as key as it has to hashable and this trasnforms it into a tuple (('a', 1), ('e', 1), ('t', 1))
            if key in hashset:
                hashset[key].append(strs[i])
            else:
                hashset[key] = [strs[i]]
                
        return_list = []
        for i in hashset.values():
            return_list.append(i)
        
        return return_list

'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we make key a hash set and group hashsets?
        hashset = {}
        
        for i in range(len(strs)):
            temp = 1
            for j in range(len(strs[i])):
                temp *= ord(strs[i][j])

            if temp in hashset:
                hashset[temp].append(strs[i])
            else:
                hashset[temp] = [strs[i]]

        print(hashset)

        return [[]]


'''
