class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hmap = {}
        t_hmap = {}

        if len(s) != len(t):
            return False
        
        for char in s:
            if char in s_hmap:
                s_hmap[char] += 1
            else:
                s_hmap[char] = 1
        
        for char in t:
            if char in t_hmap:
                t_hmap[char] +=1
            else:
                t_hmap[char] = 1
        
        return s_hmap == t_hmap
