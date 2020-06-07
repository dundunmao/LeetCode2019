class FreqStack:

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.maxfreq = 0

    def push(self, x: int) -> None:
        if x in self.freq:
            self.freq[x] += 1
        else:
            self.freq[x] = 1
        freq = self.freq[x]
        if freq in self.group:
            self.group[freq].append(x)
        else:
            self.group[freq] = [x]
        self.maxfreq = max(self.maxfreq, freq)

    def pop(self) -> int:
        res = self.group[self.maxfreq].pop()
        self.freq[res] -= 1
        if len(self.group[self.maxfreq]) == 0:
            self.maxfreq -= 1
        return res
