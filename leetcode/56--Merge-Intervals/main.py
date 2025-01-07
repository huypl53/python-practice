from typing import List 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort( key = lambda x: x[0])
        merged_intervals = [intervals[0]]
        for item in intervals[1:]:
            if merged_intervals[-1][1] >= item[0]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], item[1])
            else:
                merged_intervals.append(item)

        return merged_intervals
