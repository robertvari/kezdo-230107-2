import time, random, queue, threading

file_list = [
    "file1.jpg", 
    "file2.jpg", 
    "file3.jpg", 
    "file4.jpg",
    "file5.jpg",
    "file6.jpg",
    "file7.jpg",
    "file8.jpg",
    "file9.jpg",
    "file10.jpg",
]

job_queue = queue.Queue()

# add files to job_queue
for i in file_list:
    job_queue.put(i)

def image_worker():
    while not job_queue.empty():
        file_name = job_queue.get()
        print(f"Started converting {file_name}...")
        time.sleep(random.randint(5, 20))
        print(f"Task finished! {file_name}")

        job_queue.task_done()


for _ in range(100):
    t = threading.Thread(target=image_worker)
    t.start()