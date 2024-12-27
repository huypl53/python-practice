from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_map = defaultdict(int)
        for c in chars:
            char_map[c] += 1
        num_good = 0
        for word in words:
            w_chars = list(word)

            for c in set(w_chars):
                if c not in char_map:
                    break
                if w_chars.count(c) > char_map[c]:
                    break
            else:
                num_good += len(w_chars)
        return num_good
