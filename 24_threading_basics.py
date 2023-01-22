import time, random, threading


def worker1():
    print("Worker 1 started...")
    time.sleep(random.randint(1, 10))
    print("Worker 1 finished!")

def worker2():
    print("Worker 2 started...")
    time.sleep(random.randint(1, 10))
    print("Worker 2 finished!")

def worker3():
    print("Worker 3 started...")
    time.sleep(random.randint(1, 10))
    print("Worker 3 finished!")


t1 = threading.Thread(target=worker1)
t2 = threading.Thread(target=worker2)
t3 = threading.Thread(target=worker3)

t1.start()
t2.start()
t3.start()