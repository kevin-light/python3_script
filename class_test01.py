class Revers:
    def __init__(self,data):
        slef.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index -1
        return self.data(self.index)
rev = Revers('spam')
list(rev)