collection = {1,2,3,'a','b',1,'a','g'}
if 'd' in collection:
    print('yes')
print  (collection)
print(len(collection))

name = 'Jack'
print(name)
print(name[1])

name += 'a'

print(name)
print(name.split('a'))
name1 = 'Alan'
name1+= name
age = 1
test = f'My name is {name}, good to see you, {name1}, my age is {age} '
test1 = 'My name is {}, good to see you, {} '.format(name,name1)
print(test)
print(test1)



d = 'test'
e = d
d+= 'asdasd'
print(e)
print(d)

testL = [1,2,3]
TestB = testL
testL.append(4)
print(TestB)