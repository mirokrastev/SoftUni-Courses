import time

def exec_time(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        return end - start

    return wrapper