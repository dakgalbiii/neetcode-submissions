class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_map = {}
        for c in s:
            if c in s_map:
                s_map[c] += 1
            else:
                s_map[c] = 1
        
        for c in t:
            if c in s_map:
                s_map[c] -= 1
                if (s_map[c] < 0): return False
            else:
                return False
        return True