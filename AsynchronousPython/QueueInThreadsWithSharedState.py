import  time
import  random
import queue
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from collections import deque

count = 0
job_queue = queue.Queue()
counter_queue = queue.Queue()

not_thread_save_queue = deque()


def increment_manager():
    global count
    while True:
        increment = counter_queue.get() #this is thread safe it will LOCK the queue
        old_count = count
        count = old_count + increment
        job_queue.put((f"new counter value {count}", "--------------------"))
        counter_queue.task_done() #this will release the lock
        #job_queue.task_done()


def print_manager():
    while True:
        msg = job_queue.get()
        print(msg)
        job_queue.task_done()


def increase_counter(i):
    counter_queue.put(i)

t1 = Thread(target=increment_manager, daemon=True)
t1.start()

t2 = Thread(target=print_manager, daemon=True)
t2.start()



with ThreadPoolExecutor(max_workers = 10) as pool:
    for i in range(10):
        pool.submit(lambda :increase_counter(i))

# why if join here, then the program will wait?
# this is because join wait for a thread to finish. as for this case
# t1 and t2 are both daemon thread, it will never end, so it will be there forever


# t1.join()
# t2.join()


counter_queue.join()
job_queue.join()