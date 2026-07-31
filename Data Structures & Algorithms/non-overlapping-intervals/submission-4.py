class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        res = 0
        lastEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < lastEnd:
                res += 1
                lastEnd = min(intervals[i][1], lastEnd)
            else:
                lastEnd = intervals[i][1]

        return res