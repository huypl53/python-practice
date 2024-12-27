from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        if n == 0:
            return
        result = [0] * (m+n)
        i = i0 = i1 = 0
        while i < m + n:
            if i0 == m:
                result[i] = nums2[i1]
                i1 += 1
                i += 1
                continue
            
            if i1 == n:
                result[i] = nums1[i0]
                i0 += 1
                i += 1
                continue

            if nums1[i0] < nums2[i1]:
                result[i] = nums1[i0]
                i0 += 1
            else:
                result[i] = nums2[i1]
                i1 += 1
            i += 1
        
        for i in range(m+n):
            nums1[i] = result[i]
        

