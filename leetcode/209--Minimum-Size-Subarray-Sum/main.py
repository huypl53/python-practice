from typing import List 
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # positive nums

        n = len(nums)
        if nums[0] >= target: return 1
        s = nums[0]
        i_start = 0
        i_end = 1

        min_len = float('inf')

        while i_end < n:
            s += nums[i_end]
            if s >= target:

                while s >= target:
                    s -= nums[i_start]
                    i_start += 1
                i_start -= 1
                s += nums[i_start]        

                if i_end - i_start + 1 < min_len:
                    min_len = i_end - i_start + 1
                    if i_end == n - 1: return min_len
            # else: pass
            i_end += 1
        return min_len if min_len != float('inf') else 0
