class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        n_s = len(s)
        n_t = len(t)
        while i < n_s and j < n_t:
            if t[j] == s[i]:
                i += 1
            j += 1
        
        return i == n_s
