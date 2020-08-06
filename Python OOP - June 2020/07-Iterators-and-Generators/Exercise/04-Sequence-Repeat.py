class sequence_repeat:
    def __init__(self, seq, num):
        self.seq = seq
        self.num = num
        self.inx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 0:
            raise StopIteration
        if self.inx >= len(self.seq):
            self.inx = 0
        i = self.inx
        self.inx += 1
        self.num -= 1
        return self.seq[i]