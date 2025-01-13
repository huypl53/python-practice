class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splits = s.split()
        return len(splits[-1]) if len(splits) else 0
        
