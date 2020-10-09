class RecentCounter(object):
    pings = []
    def __init__(self):
        self.pings = []
    def ping(self, t):
        self.pings.append(t)
        rangeEnd = t - 3000
        while(self.pings[0] < rangeEnd):
            self.pings.pop(0)
        return len(self.pings)