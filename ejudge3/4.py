class H:
    def __init__(self):
        self.s = ""
    def g(self):
        self.s = input()
    def p(self):
        print(self.s.upper())
o = H()
o.g()
o.p()