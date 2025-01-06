class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i_start = -1
        n = len(gas)
        if n == 1:
            if gas[0] >= cost[0]:
                return 0
            else: return -1
        i = 0
        while i < n:
            storage = gas[i]
            i_current = i
            for j in range(1, n):
                j_next = (i+j) % n
                storage -= cost[i_current]
                if storage < 0:
                    if i_current >= i:
                        i = i_current
                    break
                storage = storage  +  gas[j_next]
                i_current = j_next
            else:
                if (j_next+1)%n == i and storage >= cost[j_next]:
                    return i
            i += 1
        return -1
