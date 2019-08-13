class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        sort = sorted(intervals, key= lambda interval:interval[0])
        meeting_room = [-1]
        for interval in sort:
            find = False
            for i in range(len(meeting_room)):
                if interval[0]>=meeting_room[i]:
                    meeting_room[i] = interval[1]
                    find = True
                    break
            if not find:
                meeting_room.append(interval[1])
            print(meeting_room)
        return len(meeting_room)

#faster
class Solution(object):
     def minMeetingRooms(self, intervals):
        starts = []
        ends = []
        for i in intervals:
            starts.append(i[0])
            ends.append(i[1])
        
        starts.sort()
        ends.sort()
        s = e = 0
        numRooms = available = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                if available == 0:
                    numRooms += 1
                else:
                    available -= 1
                    
                s += 1
            else:
                available += 1
                e += 1
        
        return numRooms