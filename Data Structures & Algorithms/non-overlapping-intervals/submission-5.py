class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def custom_sort(x):
            return x[0]
        
        intervals.sort(key = custom_sort)
        lastEnd = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < lastEnd:
                res += 1
                lastEnd = min(lastEnd, end)
            else:
                lastEnd = end

        return res