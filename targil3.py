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

# Question 6.1
