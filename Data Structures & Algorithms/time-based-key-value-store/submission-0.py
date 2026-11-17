class TimeMap(object):

    def __init__(self):
        from collections import defaultdict
        self.buckets = defaultdict(list)

    def set(self, key, value, timestamp):
        self.buckets[key].append([value, timestamp])

    def get(self, key, timestamp):
        res = ""
        values = self.buckets[key]
        b, e = 0, len(values) - 1
        while b <= e:
            m = (b + e) // 2
            if timestamp >= values[m][1]:
                res = values[m][0]
                b = m + 1
            else:
                e = m - 1
        return res