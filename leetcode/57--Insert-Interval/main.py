
from typing import List, Union

def merge_intervals(interval1: List[int], interval2: List[int]) -> Union[None, List[int]]:
    s = min(interval1[0], interval2[0])
    e = max(interval1[1], interval2[1])
    if e - s > (interval1[1] - interval1[0]) + (interval2[1] - interval2[0]):
        return 
    return [s, e]

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        merged_intervals = []
        inserted = False
        while i < len(intervals):
            result = merge_intervals(newInterval, intervals[i])
            # print(merged_intervals, i, intervals, result)

            if result is None:
                if inserted:
                    merged_intervals.append(newInterval)
                    merged_intervals += intervals[i:]
                    break
                if newInterval[0] < intervals[i][0]:
                    merged_intervals.append(newInterval)
                    merged_intervals += intervals[i:]
                    break

                merged_intervals.append(intervals[i])
            else:
                inserted = True
                newInterval = result

            i += 1

        if i == len(intervals): merged_intervals.append(newInterval)
        return merged_intervals
