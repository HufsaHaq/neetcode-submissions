class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 2 hashsets , compare if theyre equal 

        s_ = {}
        t_ = {}

        for i in s:
            s_[i] = 1 + s_.get(i,0)

        for i in t:
            t_[i] = 1 + t_.get(i,0)   

        if t_ == s_:
            return True

        return False    