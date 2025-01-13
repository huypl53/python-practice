from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_empty_len = 0
        num_seat = len(seats)
        
        head_empty = 0
        tail_empty = 0

        if seats[0] == 0:
            for s in seats:
                if s == 0:
                    head_empty += 1
                else: break
        if head_empty >= (num_seat + 1) // 2:
            return head_empty
        
        if seats[-1] == 0:
            for s in seats[::-1]:
                if s == 0:
                    tail_empty += 1
                else:
                    break
        if tail_empty >= (num_seat + 1) // 2:
            return tail_empty

        see_empty = False
        current_empty = 0
        
        for s in seats:
            # print(s, see_empty, max_empty_len, current_empty)
            if s:
                if see_empty:
                    max_empty_len = max(max_empty_len, current_empty)
                    current_empty = 0
                see_empty = False
                
            else:
                if see_empty:
                    current_empty += 1
                
                else:
                    current_empty = 1
                see_empty = True
        return max((max_empty_len+3)//2 - 1, head_empty, tail_empty)
