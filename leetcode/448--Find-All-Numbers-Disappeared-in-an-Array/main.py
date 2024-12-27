from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        uniq_nums = set(nums)
        sequence = set(range(1, n+1))
        return list(sequence - uniq_nums)
