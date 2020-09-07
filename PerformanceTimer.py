import time
verbose = False


def timeit(func):
    times_executed = 0
    total_time = 0

    def wrapper(*args, **kwargs):
        nonlocal times_executed, total_time
        if verbose:
            print('starting to record time for', func.__name__)
        start = time.time()
        return_val = func(*args, **kwargs)
        end = time.time()
        times_executed += 1
        total_time += end - start
        print('func:%s  |  time elapsed:%f  |  total time:%f  |  executed:%d  |  average:%f' %
              (func.__name__, (end - start)*1000, total_time*1000, times_executed, total_time/times_executed*1000))
        return return_val
    return wrapper
