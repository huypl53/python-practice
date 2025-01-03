from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        
        end=0
        furthest_location = 0
        min_steps = 0

        for i in range(n):
            furthest_location = max(furthest_location, nums[i] + i)
            if i >= end:
                min_steps += 1
                end = furthest_location
                if furthest_location >= n-1:
                    return min_steps
        return min_steps



    def jump_v0(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        min_jumps = [0] * n
        min_jumps[-1] = 0
        for i in range(n-2, -1, -1):
            i_jump = float('inf')
            if nums[i] == 0:
                min_jumps[i] = i_jump
                continue
            for j in range(i+1, min(n, nums[i] + i + 1)):
                if min_jumps[j] < i_jump:
                    i_jump = min_jumps[j]
            min_jumps[i] = i_jump+1
        return min_jumps[0]
