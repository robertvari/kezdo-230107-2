import time, random

def my_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Process time: {time.time() - start}")

        return result
    return wrapper

def do_nothing(func):
    def wrapper(*args, **kwargs):
        print(f"Hello. I do nothing :))) :P")
        func(*args, **kwargs)
    return wrapper

@do_nothing
@my_timer
def worker1():
    print("Worker 1 started...")
    time.sleep(random.randint(1, 10))
    print("Worker 1 finished!")

@my_timer
def worker2():
    print("Worker 2 started...")
    time.sleep(random.randint(1, 10))
    print("Worker 2 finished!")

@my_timer
@do_nothing
def worker3():
    print("Worker 3 started...")
    time.sleep(random.randint(1, 10))
    print("Worker 3 finished!")


worker1()
worker2()
worker3()