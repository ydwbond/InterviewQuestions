"""
important! need to protect from recursively call __main__

https://stackoverflow.com/questions/18204782/runtimeerror-on-windows-trying-python-multiprocessing

On Windows the subprocesses will import (i.e. execute) the main module at start.
ou need to insert an if __name__ == '__main__': guard in the main module to avoid creating subprocesses recursively.

the __name__ in the sub process will become __mp_main__
"""



import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def complex_calculator():
    start = time.time()
    print("start calculation")
    [ x ** 2 for x in range(20000000) ]
    end = time.time()
    print(f"complex_calculator take {end - start}")
    print(__name__)


def wait_for_seconds():
    time.sleep(10)

if __name__ == "__main__":

    """
    single threaded
    """
    start = time.time()
    complex_calculator()
    wait_for_seconds()
    end = time.time()
    print(f"single threaded {end-start}")


    """
    multi thread, with one wait
    """
    start = time.time()
    with ThreadPoolExecutor(max_workers = 2) as pool:
        pool.submit(complex_calculator)
        pool.submit(wait_for_seconds)

    end = time.time()
    print(f"multi thread, with one wait {end-start}")


    """
    multi thread, both workers
    """
    start = time.time()
    with ThreadPoolExecutor(max_workers = 2) as pool:
        pool.submit(complex_calculator)
        pool.submit(complex_calculator)
    end = time.time()
    print(f"multi thread, both workers {end-start}")


    """
    multi process, one wait
    """
    start = time.time()
    with ProcessPoolExecutor(max_workers = 2) as pool:
        pool.submit(complex_calculator)
        pool.submit(wait_for_seconds)
    end = time.time()
    print(f"multi process, one wait {end - start}")


    """
    multi process, both workers
    """
    start = time.time()
    with ProcessPoolExecutor(max_workers = 2) as pool:
        pool.submit(complex_calculator)
        pool.submit(complex_calculator)
    end = time.time()
    print(f"multi process, both workers {end - start}")










