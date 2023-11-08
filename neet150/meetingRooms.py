class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sort the list of intervals (0 log n) by the start time 
        intervals.sort(key = lambda i: i[0])

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]
            
            if i1[1] > i2[0]:
                return False

        return True  