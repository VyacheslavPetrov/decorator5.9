import time

def time_this(fn):
    def wrapper(NUM_RUNS):
        avg_time = 0
        for n in range(NUM_RUNS):
            t0 = time.time()
            fn(NUM_RUNS)
            t1 = time.time()
            avg_time += (t1 - t0)
        avg_time /= (NUM_RUNS)
        print("Выполнение заняло %.5f секунд" % avg_time)
    return wrapper

@time_this
def f(NUM_RUNS):
    for j in range(1000000):
        pass

f(10)