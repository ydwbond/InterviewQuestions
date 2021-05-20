def num_to_100():
    i = 0
    while i < 100:
        yield i
        i+= 1


class HundredNumGen:
    def __init__(self):
        self.anchor = 0

    def __next__(self):
        if self.anchor < 100:
            num = self.anchor
            self.anchor += 1
            return num
        else:
            raise StopIteration("reached to top")
    def __iter__(self):
        return self

a = HundredNumGen()
#print(sum(a)) #sum will bring to the end!
print(next(a))

print(next(a))
print(next(a))
print(next(a))

print('-----------------------------')
for i in a:
    print(i)




