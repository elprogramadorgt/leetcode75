import time
import tracemalloc


def test_performance(func, *args):

    tracemalloc.start()  # Start tracing memory allocations
    start_time = time.time()  # Start time measurement

    result = func(*args)  # Execute the function

    elapsed_time = time.time() - start_time  # Calculate elapsed time
    current, peak = tracemalloc.get_traced_memory()  # Get memory usage
    tracemalloc.stop()  # Stop tracing memory allocations

    print(f"Execution Time: {elapsed_time} seconds")
    print(f"Initial Memory: {current} bytes")
    print(f"Final Memory: {peak} bytes")
    print(f"Memory Usage: {peak-current} bytes")

    return elapsed_time, current, peak, peak-current

