from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in strs:
            alphabet = [0] * 26
            for j in i:
                alphabet[ord(j) - ord('a')] += 1
            key = tuple(alphabet)
            hashmap[key].append(i) 
        results = []
        for i in hashmap.values():
            results.append(i)
        return results
        