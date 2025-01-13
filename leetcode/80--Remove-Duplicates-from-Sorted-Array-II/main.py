from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if not n: return 0
        group = 2
        i = 0
        last_j = 0 

        for j in range(1, n):
            if nums[i] != nums[j]:
                d = min(j-last_j, group)
                nums[i: i+d] = [nums[i]] * d
                i += d
                nums[i] = nums[j]
                last_j = j
        for k in range(last_j, min(last_j + group, n)):
            nums[i] = nums[k]
            i += 1

        return i
