from datetime import  datetime, timezone
import time

print(datetime.now())

print(datetime.now(timezone.utc))


def powers(limit:int):
    return [x**2 for x in range(0,limit)]

start = time.time()
powers(10000)
end = time.time()

print(end-start)


#decorators

def mesure_time(func):
    start = time.time()
    func()
    end = time.time()
    print(f"your function {func.__name__} runs in {end - start} seconds")


def power(base,n):
    return base**n

def power_of_four(n):
    return 4**n

mesure_time(lambda :power(4,100000000))
mesure_time(lambda :power_of_four(100000000))

import re

string = "we are we are we are 12 "

lookingfor = '[0-9]'

print(re.findall(lookingfor,string))