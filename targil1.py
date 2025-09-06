# Question 1.a
def get_penta_num(n):
    return n * (3 * n - 1) // 2

# Question 1.b
def pentaNumRange(n1,n2):
    return list(map(get_penta_num, range(n1,n2)))

# Question 2
def sum_digit(input_str):
    input_str = input_str.strip()
    if input_str.startswith('-'):
        digits = input_str[1:]
    else:
        digits = input_str

    if not digits.isdigit():
        return "invalid input"

    return sum(map(int, digits))


num_str = input("enter number: ")
print(sum_digit(num_str))

# Question 3
def gematria_value(word):
    gematria = {
        'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10, 'כ': 20, 'ל': 30,
        'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90, 'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400,
        'ך': 20, 'ם': 40, 'ן': 50, 'ף': 80, 'ץ': 90
    }
    return sum(map(lambda letter: gematria.get(letter, 0), word))

print(gematria_value("שיראל"))  # Output: 541

# Question 4.a
def is_prime(n):
    if n < 2:
        return False
    div = range(2, int(n**0.5) + 1)
    checks = map(lambda i: n % i != 0, div)
    return all(checks)

print(is_prime(11))  # Output: True

# Question 4.b
def twin_prime(p):
    if not is_prime(p):
        return "invalid input"
    if is_prime(p + 2):
        return p + 2
    if is_prime(p - 2):
        return p - 2
    return "invalid input"

num_str = input("enter prime number:\n").strip()

if not num_str.lstrip('-').isdigit():
    print("invalid input")
else:
    num = int(num_str)
    print(twin_prime(num))

# Question 6.a
multiply_by_2 = lambda x: x * 2
square = lambda x: x ** 2
hofchi = lambda x: 1 / x

functions = [multiply_by_2, square, reciprocal]

# Question 6.b - פונקציה שמקבלת מספרים ורשימת פונקציות ומחזירה מילון
apply_functions = lambda numbers, funcs: dict(
    zip(
        map(lambda f: f.__name__, funcs),
        map(lambda f: list(map(f, numbers)), funcs))
)

# Question 5
