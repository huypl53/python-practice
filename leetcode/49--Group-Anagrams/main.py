from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_grams = defaultdict(list)
        for s in strs:
            hash_grams["".join(sorted(s))].append(s)
        return list(hash_grams.values())
