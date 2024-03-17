import timeit

code1 = """\
return " ".join(s.split()[::-1])
"""

code2 = """\
queue = deque()
start = 0
i = 0
while i < len(s):
    # ... (rest of the second approach)
return " ".join(queue)
"""

setup = "from collections import deque"

time1 = timeit.timeit(code1, number=10000, setup=setup)
time2 = timeit.timeit(code2, number=10000, setup=setup)

print(f"Time for Approach 1: {time1}")
print(f"Time for Approach 2: {time2}")