
from typing import List

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
        if len(security) < 2 * time + 1: return []
        n = len(security)
        if not time: return list(range(n))
        
        forward = [0] * n
        backward = [0] * n
        valid_days = []

        for i in range(1, n-1):
            if security[i] <= security[i-1]: forward[i] = forward[i-1] + 1
            j = n - i
            if security[j] >= security[j-1]: backward[j-1] = backward[j] + 1
        
        for i in range(n):   
            if forward[i] >= time and  backward[i] >= time:
                valid_days.append(i)
        return valid_days
