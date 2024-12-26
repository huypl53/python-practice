from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # k = k % n
        # while k > 0:
        #     i = nums.pop()
        #     nums.insert(0, i)
        #     k -= 1

        n = len(nums)
        k = k % n
        d = n - k

        result = []
        for i in range(n):
            result.append(nums[(d+i)%n])
        
        for i in range(n):
            nums[i] = result[i]

