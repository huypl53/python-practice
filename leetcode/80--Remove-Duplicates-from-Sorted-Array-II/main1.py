from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        max_seq = 2
        pre_idx = list(range(max_seq))
        for v in nums:
            if i in pre_idx or nums[i-max_seq] != v:
                nums[i] = v
                i += 1

        return i
