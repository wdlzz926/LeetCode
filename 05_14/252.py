class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        sort = sorted(intervals,key = lambda interval: interval[0])
        for i in range(len(sort)-1):
            if sort[i][1] > sort[i+1][0]:
                return False
        return True
        