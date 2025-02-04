from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        max_inc_len = max_dec_len = 1
        inc_len = 1
        dec_len = 1
        end = 1

        while end < n:
            if nums[end] > nums[end - 1]:
                inc_len += 1
                dec_len = 1
            elif nums[end] < nums[end - 1]:
                dec_len += 1
                inc_len = 1
            else:
                dec_len = inc_len = 1
            if inc_len > max_inc_len:
                max_inc_len = inc_len
            if dec_len > max_dec_len:
                max_dec_len = dec_len

            end += 1
        return max(max_inc_len, max_dec_len)
