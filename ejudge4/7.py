class R:
    def __init__(self, s):
        self.s = s
        self.i = len(s) - 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < 0:
            raise StopIteration
        r = self.s[self.i]
        self.i -= 1
        return r
m = input()
it = R(m)
for c in it:
    print(c, end='')