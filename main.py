
class Status:
    def __init__(self, l):
        self.cummulative = [0] * len(l)
        self.cummulative[0] = l[0]
        for index, value in enumerate(l[1:], 1):
            self.cummulative[index] = self.cummulative[index - 1] + value
        self.total = sum(l)

    def less(self, n):
        return self.cummulative[n - 1] if n  > 0 else 0

    def greater(self, n):
        return self.total - self.cummulative[n + 1]

    def between(self, start, end):
        return self.less(end + 1) - self.less(start - 1)

class DataCapture:
    def __init__(self, n=1000):
        self.l = [0] * n

    def add(self, value):
        self.l[value] += 1

    def build_stats(self):
        return Status(self.l)


capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()
print(stats.less(4))
print(stats.between(3, 6))
print(stats.greater(4))