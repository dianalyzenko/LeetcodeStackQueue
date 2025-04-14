from collections import defaultdict

class FreqStack(object):

    def __init__(self):
        self.counts = defaultdict(int)
        self.levels = defaultdict(list)
        self.top_freq = 0   

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.counts[val] += 1
        freq = self.counts[val]
        if freq > self.top_freq:
            self.top_freq = freq
        self.levels[freq].append(val)

    def pop(self):
        """
        :rtype: int
        """
        val = self.levels[self.top_freq].pop()
        self.counts[val] -= 1
        if not self.levels[self.top_freq]:
            self.top_freq -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()