import time, random

def worker():
    print("Worker started...")
    time.sleep(random.randint(1, 10))
    print("Worker finished!")

start = time.time()
worker()
print(f"Process time: {time.time() - start}")