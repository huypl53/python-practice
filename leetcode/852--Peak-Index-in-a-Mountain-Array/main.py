from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 5:
            maxx = -(float('inf'))
            k = -1
            for i, v in enumerate(arr):
                if v > maxx:
                    maxx = v
                    k = i
            return k
        start = 0
        end = n-1
        middle = (end + start)//2

        while start < end:
            if arr[middle] < arr[middle+1]:
                start = middle+1
            else:
                end = middle
            middle = (end + start) // 2
        return start
            

