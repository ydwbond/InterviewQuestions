"""decorator function not working in the target of thread, will get back to main
pure wait function will benefit from multithreading
working fuction will not

#GIL
is a lock for thread prevent from ture multi tasking
"""


import time
import threading
from concurrent.futures import ThreadPoolExecutor

def time_and_run(func):
    start = time.time()
    func()
    end = time.time()
    print(f"{func.__name__} took {end-start} second")


def ask_user():
    user_input = input("enter your name ")
    greet = f"Hello {user_input}"
    print(f"{greet} from {threading.currentThread().getName()}")


def pure_wait(second):
    time.sleep(second)
    print(f"from {threading.currentThread().getName()}")


def power_with_base (base,n):
    print(f"from {threading.currentThread().getName()}")
    return [ x ** 2 for x in range(20000000) ]


start = time.time()
# time_and_run(ask_user)
# time_and_run(lambda :pure_wait(2))
# time_and_run(lambda :power_with_base(5,1000000))

#pure_wait(10)
pure_wait(10)
power_with_base(5,100000000)
end = time.time()
print(end-start)

start = time.time()
#th1 = threading.Thread(target=ask_user)
th2 = threading.Thread(target= lambda : pure_wait(10))

#looks like the decorator fucntion will go back to main thread
#th3 = threading.Thread(target=time_and_run(lambda :power_with_base(5,1000000)))
th3 = threading.Thread(target=lambda :power_with_base(5,1000000))

#th1.start()
th2.start()
th3.start()
#th1.join()
th2.join()
th3.join()
end = time.time()
print(end-start)

start = time.time()

with ThreadPoolExecutor(max_workers = 2) as pool:
    pool.submit(lambda : pure_wait(10))
    pool.submit(lambda :power_with_base(5,1000000))
end = time.time()
print(end-start)


