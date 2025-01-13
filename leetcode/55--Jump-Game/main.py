from typing import List 

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0: return True
        pos = n - 1
        for i in range(n-2, -1, -1):
            if nums[i] + i >= pos:
                pos = i

        return pos == 0
        
    def canJump1(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if not n: return False
        if n == 1: return True
        jumpNodes = [False] * n
        jumpNodes[-1] = True


        for i in range(n-2, -1, -1):
            if nums[i] + i == n - 1: 
                jumpNodes[i] = True
                continue
            for j in range(1, min(nums[i], n-i)+1):
                if jumpNodes[i+j]:
                    jumpNodes[i] = True
                    break

        return jumpNodes[0]

