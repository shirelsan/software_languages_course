# Question 1.1
def tuple_regular_rkorciya(n):
    if n == 0:
        return ()
    return (n,) + tuple_regular_rkorciya(n - 1)

# Question 1.2
def tuple_tail_rkorciya(n):
    def helper(acc, k):
        if k == 0:
            return acc
        return helper(acc + (k,), k - 1)
    return helper((), n)

# Question 2
def sum_regular_rkorciya(arr):
    if not arr:  # מקרה בסיס
        return 0
    return arr[0] + sum_regular_rkorciya(arr[1:])

def sum_tail_rkorciya(arr):
    def helper(acc, rest):
        if not rest:
            return acc
        return helper(acc + rest[0], rest[1:])
    return helper(0, arr)

# Question 3.1
def gcd_regular_rkorciya(a, b):
    if b == 0:
        return a
    return gcd_regular_rkorciya(b, a % b)

def lcm_regular_rkorciya(a, b):
    return abs(a * b) // gcd_regular_rkorciya(a, b)

# Question 3.2
def gcd_tail_rkorciya(a, b):
    def helper(x, y):
        if y == 0:
            return x
        return helper(y, x % y)  # קריאת זנב
    return helper(a, b)

def lcm_tail_rkorciya(a, b):

    return abs(a * b) // gcd_tail_rkorciya(a, b)

# Question 4.1
def isPalindrome_regular(n):
    s = str(n)
    def helper(s):
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return helper(s[1:-1])  # מקצר משני הצדדים של הפילנדרום
    return helper(s)

# Question 4.2 // עם מצבעים 
def isPalindrome_tail(n):
    s = str(n)
    def helper(left, right):
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return helper(left + 1, right - 1)  # קריאת זנב
    return helper(0, len(s) - 1)

# Question 5.1
def sortedzip_regular(lists):
    if not lists:
        return zip()
    first_sorted = sorted(lists[0])
    rest_sortedzip = sortedzip_regular(lists[1:])
    return zip(first_sorted, *rest_sortedzip)

# Question 5.2
def sortedzip_tail(lists):
    def helper(acc, remaining):
        if not remaining:
            return zip(*acc)
        return helper(acc + [sorted(remaining[0])], remaining[1:])
    return helper([], lists)

# Lazy Evaluation, Generators
# Question 1
def build_array_eager():
    start = time.time()
    arr = list(range(10001))
    end = time.time()
    print("זמן יצירה (eager):", end - start)
    print("גודל בזיכרון:", sys.getsizeof(arr))
    print("type:", type(arr))
    return arr

def build_array_lazy():
    start = time.time()
    arr = (i for i in range(10001))
    end = time.time()
    print("זמן יצירה (lazy):", end - start)
    print("גודל בזיכרון:", sys.getsizeof(arr))
    print("type:", type(arr))
    return arr

def first_half_eager():
    full = list(range(10001))
    start = time.time()
    arr = full[:5000]
    end = time.time()
    print("זמן חיתוך (eager):", end - start)
    print("גודל בזיכרון:", sys.getsizeof(arr))
    print("type:", type(arr))
    return arr

def first_half_lazy():
    full = (i for i in range(10001))
    start = time.time()
    arr = islice(full, 5000)
    end = time.time()
    print("זמן חיתוך (lazy):", end - start)
    print("גודל בזיכרון:", sys.getsizeof(arr))
    print("type:", type(arr))
    return arr

# Question 2 // פתרון רקורסיבי - פונקציונלי 
def prime_generator_recursive(start=2):
    
    def is_prime(n, divisor=2):
        if n < 2:
            return False
        if divisor * divisor > n:
            return True
        if n % divisor == 0:
            return False
        return is_prime(n, divisor + 1)

    if is_prime(start):
        yield start

    # קריאה רקורסיבית להמשך
    yield from prime_generator_recursive(start + 1)

# Question 3 
def taylor_series_recursive(x, k=0, term=1.0, sum_so_far=0.0):
    sum_so_far += term
    yield sum_so_far 

    # קריאה רקורסיבית עם האיבר הבא: x^(k+1)/(k+1)!
    yield from taylor_series_recursive(x, k + 1, term * x / (k + 1), sum_so_far)

 """
x = 2
gen = taylor_series_recursive(x)

for _ in range(8):
    print(next(gen))
פלט:
1.0
3.0
5.0
6.333333333333333
7.0
7.266666666666667
7.355555555555555
7.3809523809523805
 """
