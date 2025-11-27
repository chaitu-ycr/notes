# ⚡ Usecase: True Parallelism with `multiprocessing`

Your computer has multiple CPU cores, but by default, a standard Python program only runs on one at a time. This is because of a mechanism called the **Global Interpreter Lock (GIL)**, which prevents multiple threads from executing Python bytecode simultaneously.

So, how do you make your Python code truly run in parallel to take full advantage of modern hardware for CPU-intensive tasks (like data processing, mathematical computations, or video encoding)? The answer is the `multiprocessing` module.

---

## 🎯 Multiprocessing: Practical, Tricky, and Fun Usages

```python
# ===== 1. Basic Process =====
import multiprocessing
import os
import time
def worker(name):
    print(f"Start {name} (PID: {os.getpid()})")
    time.sleep(1)
    print(f"End {name}")
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=worker, args=("A",))
    p2 = multiprocessing.Process(target=worker, args=("B",))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

# ===== 2. Pool for Parallel Map =====
def square(x):
    return x * x
if __name__ == '__main__':
    with multiprocessing.Pool(4) as pool:
        nums = [1,2,3,4,5]
        results = pool.map(square, nums)
    print(results)

# ===== 3. Sharing Data with Queue =====
def producer(q):
    q.put([42, None, "hello"])
def consumer(q):
    print(q.get())
if __name__ == '__main__':
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

# ===== 4. Fun: Parallel Factorial Calculation =====
def factorial(n):
    return 1 if n==0 else n*factorial(n-1)
if __name__ == '__main__':
    with multiprocessing.Pool(4) as pool:
        nums = [5, 6, 7, 8]
        facts = pool.map(factorial, nums)
    print(facts)

# ===== 5. Using Manager for Shared State =====
def update(shared):
    shared.value += 1
if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    shared = mgr.Namespace()
    shared.value = 0
    procs = [multiprocessing.Process(target=update, args=(shared,)) for _ in range(5)]
    for p in procs: p.start()
    for p in procs: p.join()
    print(shared.value)

# ===== 6. Exception Handling in Processes =====
def risky():
    raise RuntimeError("Oops!")
if __name__ == '__main__':
    p = multiprocessing.Process(target=risky)
    p.start()
    p.join()
    print("Process finished (may have errored)")

# ===== 7. Pro-Tips =====
# Always use 'if __name__ == "__main__"' guard
# Use Pool for many tasks
# Use Queue/Manager for sharing data
# Processes have separate memory spaces
```
