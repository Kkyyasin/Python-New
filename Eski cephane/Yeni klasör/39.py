#itaberle
liste=[x for x in range(1000)]
a=iter(liste)
while True:
    try:
        print(next(a))
    except StopIteration:
        break
class iterobje():
    def __init__(self,max,min=0):
        self.min=min
        self.max=max
    def __iter__(self):
        return  self
    def __next__(self):
        if self.min<=self.max:
            self.min+=1
            print(self.min)
        else:
            raise StopIteration()
a=iterobje(100)
while True:
    try:
     next(a)
    except StopIteration:
        break