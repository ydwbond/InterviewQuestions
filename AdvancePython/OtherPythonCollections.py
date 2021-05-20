"""
* counter
* defualtdict
* ordereddict
* namedtuple
* deque
"""

from collections import Counter
from collections import defaultdict

ages = [10,11,20,12,3,35,1,98,1,20,10,20,12,1,29]
print(Counter(ages))
print(Counter(ages)[20])

t1 = Counter({"hello":5,"world":10})
print(t1['world'])


coworkers = [("Tom",10),("Jim",20),("Tim",30),("Tom",20),("Sam",15)]

result ={}

for name, times in coworkers:
    if name not in result:
        result[name] = [times]
    else:
        result[name].append(times)

print(result['Tom'])
#print(result['jack']) # this will error, due to no key found


result = defaultdict(list)

for name, times in coworkers:
    result[name].append(times)

#print(result)

 # this will not error as there the dict has a default value of list
print(result["Jack"])
#by executing result["Jack"], it will add Jack to the dict with a value of empty list
print(result)
result.default_factory = int
#at here , even the default_factory changes to int, it will not affect Jack as Jack is already in the dict
#so this time the out put of this is still []
print(result["Jack"])

#at this time, a new key will return 0
print(result['John'])

print(result)

comp = "arrowStreet"
colleague = ("Tim", "Tom", "Jim", "Sam")
other_person = [("Jack", "Apple Inc"), ("Jill", "Google inc")]

r = defaultdict(lambda :comp)

for name, company in other_person:
    r[name] = company

print(r)

print(r["Tim"])
print(r)


#named tuple
from collections import namedtuple


t = ("checking", 100.98)

Checking = namedtuple("Checking",['name','balance'])

c = Checking("checking", 100.98)
print(c)

print(c.balance)

coworkers = [("Tom",10),("Jim",20),("Tim",30),("Sam",15)]

Cowork = namedtuple("Cowork",['name','age'])

rm = []
for c in coworkers:
    print(Cowork._make(c))
    rm.append(Cowork(*c))

print(rm[0].name, rm[0].age)
print(rm[0]._asdict())
print(rm)



#double ended queue
#threads safe


from collections import  deque

colleague = ("Tim", "Tom", "Jim", "Sam")

de_co = deque(colleague)

print(de_co)

de_co.append("Jack")
de_co.appendleft("Ison")
de_co.append("Tom")
print(de_co)
de_co.pop()
de_co.pop()
de_co.popleft()
print(de_co)









