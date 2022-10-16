class DefaultList(list):
    def __init__(self, default_val = 1):
        super().__init__(self)
        self.default = default_val
    
    def __getitem__(self, idx):
        try:
            return super().__getitem__(idx)
        except IndexError:
            return self.default

s = DefaultList(5)
s.extend([4, 10])
indexes = [1, 124, 1882]
for i in indexes:
    print(s[i], end=" ")

