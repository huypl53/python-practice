class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        c_map = defaultdict(int)
        for s_c, t_c in zip(s, t):
            c_map[s_c] += 1
            c_map[t_c] -= 1

        for v in c_map.values():
            if v != 0: return False
        else: return True
