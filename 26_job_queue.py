import time, random

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

def image_worker(file_name):
    print(f"Started converting {file_name}...")
    time.sleep(random.randint(5, 20))
    print(f"Task finished!")