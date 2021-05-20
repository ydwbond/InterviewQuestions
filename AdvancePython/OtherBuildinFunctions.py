class Num_Iter:
    def __init__(self, start: int):
        self.start = start
        self.current = start

    def __next__(self):
        if self.current < 100:
            i = self.current
            self.current += 1
            return i
        else:
            raise StopIteration("reached to the top")

    def __iter__(self):
        return self


num = Num_Iter(10)
i = filter(lambda x: x % 2 == 0, num)
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(list(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


# find the even numbers
num = list(range(0,100))

#first way
f = filter(lambda x: x % 2 == 0, num)

#second_way generator comprehension
g = (x for x in num if x % 2 == 0)

#third way:
def find_out_even_number(func, num):
    for i in num:
        if func(i):
            yield i
fun = find_out_even_number(lambda x : x % 2 ==0 , num)

print(next(f))
print(next(g))
print(next(fun))

print(next(f))
print(next(g))
print(next(fun))


# add 5 to each number of the list
m = map(lambda x: x + 5, num)
g1 = (x+5 for x in num)
def add_5_to_number(func, num):
    for i in num:
        yield func(i)

fun1 = add_5_to_number(lambda x: x+5, num)

print(next(m))
print(next(g1))
print(next(fun1))

print(next(m))
print(next(g1))
print(next(fun1))

list = [0,1,2,3,4,5]
print(all(list))
print(any(list))