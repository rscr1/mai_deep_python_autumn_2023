import time


def mean(k: int):
    """
    decorator that output average time of last k calls
    :param k: last k calls 
    :return: decorator
    """
    def decorator(func):
        sample: list = []
        def wrapper_func(*args, **kwargs):
            start: float = time.time()
            result = func(*args, **kwargs)
            end: float = time.time()
            sample.append(end - start)
            if len(sample) > k:
                sample.pop(0)
            mean_time: float = .0
            if sample:
                mean_time: float = sum(sample) / len(sample)
            print(f"Mean time of last {k} calls: {mean_time:.4f}s")

            return result
        return wrapper_func
    return decorator

@mean(10)
def foo():
    '''function for decorator'''
    time.sleep(0.1)

@mean(2)
def boo():
    '''function for decorator'''
    time.sleep(0.1)

for _ in range(100):
    foo()
