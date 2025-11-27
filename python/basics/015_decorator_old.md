# 🧩 Python Decorators

Decorators are Python's powerful way to modify or enhance functions and classes without changing their source code. They promote code reuse, separation of concerns, and expressive, modular design. Use decorators for logging, authentication, error handling, caching, and more.

## 🎯 Python Decorator: Practical, Tricky, and Fun Usages

```python
# ===== 1. Basic Decorator =====
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
say_hello()

# ===== 2. Decorator with Arguments =====
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(3)
def greet():
    print("Hi!")
greet()

# ===== 3. Logging Decorator =====
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b
add(2, 3)

# ===== 4. Stacking Multiple Decorators =====
def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclaim(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!"
    return wrapper

@exclaim
@uppercase
def greet(name):
    return f"hello {name}"
print(greet("world"))

# ===== 5. Decorator for Timing =====
import time
def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f}s")
        return result
    return wrapper

@timing
def slow():
    time.sleep(0.1)
slow()

# ===== 6. Decorator for Authentication =====
def authenticated(func):
    def wrapper(*args, **kwargs):
        user = kwargs.get('user', None)
        if user != 'admin':
            print("Access denied!")
            return
        return func(*args, **kwargs)
    return wrapper

@authenticated
def secret_data(user=None):
    print("Secret data!")
secret_data(user='guest')
secret_data(user='admin')

# ===== 7. Decorator for Caching =====
def cache(func):
    memo = {}
    def wrapper(x):
        if x in memo:
            print("Cache hit!")
            return memo[x]
        result = func(x)
        memo[x] = result
        return result
    return wrapper

@cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
print(fib(10))

# ===== 8. Limiting Calls Decorator =====
def limit_calls(max_calls):
    def decorator(func):
        count = [0]
        def wrapper(*args, **kwargs):
            if count[0] >= max_calls:
                print("Limit reached!")
                return
            count[0] += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator

@limit_calls(2)
def hello():
    print("Hello!")
hello()
hello()
hello()

# ===== 9. Prefix Decorator =====
def prefix(p):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return p + func(*args, **kwargs)
        return wrapper
    return decorator

@prefix("[INFO] ")
def message():
    return "System running."
print(message())
```
