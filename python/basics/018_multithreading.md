# 🧵 Usecase: Concurrent Tasks with `multithreading`

Imagine your program needs to download several files from the internet. If you do it sequentially, it will download one file, wait, download the next, wait, and so on. Most of its time is spent **waiting** for the network. This is called an **I/O-bound** task.

**Multithreading** is the perfect solution for this. It allows your program to start multiple threads of execution that can run concurrently. While one thread is "blocked" (waiting for a download to finish), another thread can run, making your application much more responsive and efficient.

---

## 🎯 Multithreading: Practical, Tricky, and Fun Usages

```python
# ===== 1. Basic Thread =====
import threading
import time
def download(name):
    print(f"Start {name}")
    time.sleep(1)
    print(f"End {name}")
t1 = threading.Thread(target=download, args=("file1",))
t2 = threading.Thread(target=download, args=("file2",))
t1.start()
t2.start()
t1.join()
t2.join()

# ===== 2. ThreadPoolExecutor =====
from concurrent.futures import ThreadPoolExecutor
def work(x):
    time.sleep(0.5)
    return x*x
with ThreadPoolExecutor(max_workers=3) as pool:
    results = pool.map(work, [1,2,3,4])
    print(list(results))

# ===== 3. Race Condition Example =====
counter = 0
def increment():
    global counter
    for _ in range(10000):
        counter += 1
threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()
print(counter)  # May be less than 50000!

# ===== 4. Lock to Prevent Race Condition =====
counter = 0
lock = threading.Lock()
def safe_increment():
    global counter
    for _ in range(10000):
        with lock:
            counter += 1
threads = [threading.Thread(target=safe_increment) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()
print(counter)  # Will be exactly 50000

# ===== 5. Fun: Download Multiple Files =====
def fake_download(name):
    print(f"Downloading {name}")
    time.sleep(0.5)
    print(f"Done {name}")
files = [f"file{i}.zip" for i in range(1, 4)]
threads = [threading.Thread(target=fake_download, args=(f,)) for f in files]
for t in threads: t.start()
for t in threads: t.join()

# ===== 6. Pro-Tips =====
# Use threads for I/O-bound tasks
# Use locks for shared data
# Use ThreadPoolExecutor for simplicity
# Threads share memory, so be careful!
```
