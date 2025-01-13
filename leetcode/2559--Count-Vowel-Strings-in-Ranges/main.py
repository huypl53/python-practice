from typing import List
vowels = ['a', 'e', 'i', 'o', 'u']

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels_accumulator = []
        count = 0
        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                count += 1 
            vowels_accumulator.append(count)
        print(vowels_accumulator)
        return [ vowels_accumulator[q[1]] - vowels_accumulator[q[0]-1] if q[0] > 0 else vowels_accumulator[q[1]] for q in queries]        
