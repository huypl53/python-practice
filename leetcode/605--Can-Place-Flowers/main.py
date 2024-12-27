from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        flower_num = len(flowerbed)
        flowerbed.insert(0, 0)
        flowerbed.append(0)

        for i in range(1, flower_num+1):
            if n == 0:
                return True
            if flowerbed[i]: continue
            if flowerbed[i-1] + flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1
        else:
            if n == 0: return True
            return False
