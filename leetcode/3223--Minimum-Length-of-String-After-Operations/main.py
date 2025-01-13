from collections import defaultdict

class Solution:
    def minimumLength(self, s: str) -> int:
        char_dict = defaultdict(int)
        for c in s:
            char_dict[c] += 1
        return sum([1 if count % 2 == 1 else 2 for count in char_dict.values()])
