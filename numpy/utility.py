import time

def time_taken(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("Time taken by ", func.__name__ ,": ", time.time() - start)
        return result
    return wrapper

def show(**items):
    for name, value in items.items():
        print(f"\n{name}: \n {value}")

