import time, random, threading


def worker1(sleep_max):
    print(f"Worker 1 started. sleep_max: {sleep_max}")
    time.sleep(random.randint(1, sleep_max))
    print("Worker 1 finished!")

def worker2(sleep_max):
    print(f"Worker 2 started. sleep_max: {sleep_max}")
    time.sleep(random.randint(1, sleep_max))
    print("Worker 2 finished!")

def worker3(sleep_max):
    print(f"Worker 3 started. sleep_max: {sleep_max}")
    time.sleep(random.randint(1, sleep_max))
    print("Worker 3 finished!")


t1 = threading.Thread(target=worker1, args=[10])
t2 = threading.Thread(target=worker2, args=[4])
t3 = threading.Thread(target=worker3, args=[30])

t1.start()
t2.start()
t3.start()