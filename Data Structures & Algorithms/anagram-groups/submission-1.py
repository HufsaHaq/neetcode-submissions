class Solution:
    def check_anagram(str1,str2):
        # this is just anagram revision not relevant to question
        if len(str1) != len(str2):
            return False
        map1 = {}
        map2 = {}
        for i in str1:
            map1[i] = 1 + map1.get(i,0)
        for i in str2:
            map2[i] = 1 + map2.get(i,0)

        for i in map1:
            if map1[i] != map2.get(i,0):
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap the key will be an array of how much of what there is
        # the value will be a list of words that have the same composition
        # eg key: 1a 1e 1t like [1,0 .... ,0 , 1,...], value: ate tea eat

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a.....z

            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        return list(res.values())
