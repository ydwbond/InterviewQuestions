list1 = [1,2,3]
list2 = [4,5,6]

t = (list1,list2)

print(t)

list1[0]= 10



print(t)
print(t[0])

t[1][1] = 100
print(t)


def func(ls):
    ls.append(10)
    return ls
print(id(list1))
test = func(list1)
print(test)
print(id(test))


print(id(None))

test1 = 1
test2 = 1

print(id(test1))
print(id(test2))
print(id(None))

print(test1 is test2)

test1 = "this is".strip()
test2 = "this is".strip()

print(test1 is test2)

str1 = "hello "
print(id(str1))
str1 += "world"
print(id(str1))