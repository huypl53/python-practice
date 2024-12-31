from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        shift = 0
        while i < n:
            v = nums[i]
            if v == val:
                shift += 1
            else:
                if shift:
                    nums[i-shift] = v
            i += 1
        
        return n - shift
