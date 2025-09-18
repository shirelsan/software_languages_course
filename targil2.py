from functools import reduce
import operator
import time

# Question 1.a
linear = lambda x: 2 + 2 * x 

# Question 1.b
nums = range(0, 10001)
mapped_tuple = tuple(map(linear, nums))

# Question 1.2
sum_with_reduce = reduce(operator.add, mapped_tuple, 0)

# Question 1.3
def time_fn(fn, repeats=5):
    times = []
    for _ in range(repeats):
        t0 = time.perf_counter()
        res = fn()
        t1 = time.perf_counter()
        times.append((t1 - t0, res))
    avg = sum(t for t, _ in times) / repeats
    return avg, times[-1][1]

# Question 1.4
def reduce_compute_and_sum():
    return reduce(lambda acc, x: acc + (2 + 2 * x), nums, 0)

# Question 2
nums = list(range(1, 1001))
# 1
evens = list(filter(lambda x: x % 2 == 0, nums))
odds  = list(filter(lambda x: x % 2 != 0, nums))

even_func = lambda seq: reduce(lambda acc, x: acc + [acc[-1] * x], seq[1:], [seq[0]])

odd_func = lambda seq: reduce(
    lambda acc, i: acc + [acc[-1] + (seq[i+1] / 2 + 2 + acc[-1])] if i+1 < len(seq) else acc,
    range(len(seq)),
    [seq[0]]
)
# 2 
even_result = even_func(evens)
odd_result  = odd_func(odds)

# 3
sum_evens = reduce(lambda a, b: a + b, even_result)
sum_odds  = reduce(lambda a, b: a + b, odd_result)

# Question 3 

def new_dates(start_date_str, count, step):
    start = int(start_date_str)
    indices = range(count)
    
    return list(map(lambda i: str(start + i*step), indices))

# Question 4.a
def power_function(exp):
    return lambda base: base ** exp

# Question 4.b
def make_powers(n):
    return lambda base: map(lambda exp: base ** exp, range(1, n + 1))

n = int(input("Enter number of powers: "))
result = make_powers(n)

print(type(result(1)))

base = int(input("Enter base: "))
print(tuple(result(base)))

# Question 4.c
def taylor_exp(x, n):
    return reduce(
        lambda acc, k: acc + (x**k) / math.factorial(k),
        range(n+1),
        0
    )

# Question 5
def task_manager():
    tasks = {}

    def add_task(name, status="incomplete"):
        tasks[name] = status

    def complete_task(name):
        if name in tasks:
            tasks[name] = "complete"

    def get_tasks():
        return tasks.copy()  # אני בכוונה מחזירה העתק כדי שלא ישתנה מבחוץ

    return {
        "add_task": add_task,
        "complete_task": complete_task,
        "get_tasks": get_tasks
    }
