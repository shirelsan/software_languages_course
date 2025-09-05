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

# Question 4
