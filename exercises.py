# =============================================================================
# Coderslab Python Prework - Exercises
# =============================================================================

# -----------------------------------------------------------------------------
# Task 1 v1: First program
# -----------------------------------------------------------------------------
print("My name is Vit")


# -----------------------------------------------------------------------------
# Task 1 v2: Using variable
# -----------------------------------------------------------------------------
name: str = "Vit"
print(f"My name is {name}")


# -----------------------------------------------------------------------------
# Task 2: Math operations
# -----------------------------------------------------------------------------
print(2 + 3)
print(10 / 4)
print(30 * 2)


# -----------------------------------------------------------------------------
# Task 3: Errors and Data Types
# -----------------------------------------------------------------------------
"Hello World"  # OK: String v dvojitých uvozovkách
"Hello World"  # OK: String v jednoduchých uvozovkách
2  # OK: Integer (celé číslo)

# hello       # CHYBA: NameError (proměnná není definována, Python nepozná, o jaký datový typ jde)


# -----------------------------------------------------------------------------
# Task 4: Data types
# -----------------------------------------------------------------------------
# Definice proměnných s typovými anotacemi
my_int: int = 42  # Celé číslo (integer)
my_float: float = 3.14  # Desetinné číslo (float)
my_str: str = "Ahoj světe"  # Textový řetězec (string)
my_multiline: str = """Toto je
víceřádkový
string."""  # Víceřádkový string
my_bool: bool = True  # Logická hodnota (boolean)

# Výpis ve formátu: variable <variable> of the <type> type.
print(f"variable {my_int} of the {type(my_int)} type.")
print(f"variable {my_float} of the {type(my_float)} type.")
print(f"variable {my_str} of the {type(my_str)} type.")
print(f"variable {my_multiline} of the {type(my_multiline)} type.")
print(f"variable {my_bool} of the {type(my_bool)} type.")

# -----------------------------------------------------------------------------
# Task 5: Addition
# -----------------------------------------------------------------------------
add1: int = 10
add2: float = 2.5
sum_value: float = add1 + add2

print(f"add1: {add1} type: {type(add1)}")
print(f"add2: {add2} type: {type(add2)}")
print(f"sum_value: {sum_value} type: {type(sum_value)}")

# -----------------------------------------------------------------------------
# Task 6: Mathematical operations
# -----------------------------------------------------------------------------
a: int = 10
b: int = 15
sum_value: int = a + b
quotus: float = b / a
int_part: int = int(quotus)

print(f"a: {a} type: {type(a)}")
print(f"b: {b} type: {type(b)}")
print(f"sum_value: {sum_value} type: {type(sum_value)}")
print(f"quotus: {quotus} type: {type(quotus)}")
print(f"int_part: {int_part} type: {type(int_part)}")

# -----------------------------------------------------------------------------
# Task 7: Adding list elements - Greek Mythology instead of animals - kontrola zda Anet dává pozor :)
# -----------------------------------------------------------------------------
mythical_beasts: list[str] = []

mythical_beasts.append("Hydra")
print(mythical_beasts)

mythical_beasts.append("Minotaur")
print(mythical_beasts)

mythical_beasts.append("Sphinx")
print(mythical_beasts)

# -----------------------------------------------------------------------------
# Task 8: Retrieving list elements
# -----------------------------------------------------------------------------
words: list[str] = [
    "is",
    "wrong",
    "dough",
    "correspondence",
    "Python",
    "snake",
    "tolerate",
    "conflict",
    "chase",
    "begin",
    "fun",
    "confidence",
    "beat",
]

# Pátý prvek (index 4)
print(f"Pátý prvek: {words[4]}")

# První prvek (index 0)
print(f"První prvek: {words[0]}")

# Třetí prvek od konce (index -3)
print(f"Třetí od konce: {words[-3]}")
# RESULT: Python is fun

# -----------------------------------------------------------------------------
# Task 9: Retrieving data from the user
# -----------------------------------------------------------------------------
first_name: str = input("What's your name: ")
surname: str = input("What's your surname: ")

print(f"{first_name} {surname} is a Python programmer!")

# -----------------------------------------------------------------------------
# Task 10: Joining a list
# -----------------------------------------------------------------------------
letters: list[str] = ["a", "b", "c", "d", "e"]
joined_string: str = " ".join(letters)

print(joined_string)

# -----------------------------------------------------------------------------
# Task 11: Modulo division
# -----------------------------------------------------------------------------
a: int = 10
b: int = 3
modulo_result: int = a % b

print(f"Zbytek po dělení {a} / {b} je: {modulo_result}")

# -----------------------------------------------------------------------------
# Task 12: Increment and decrement
# -----------------------------------------------------------------------------
counter: int = 145
print(f"Počáteční stav: {counter}")

counter += 1
print(f"Po inkrementaci: {counter}")

counter -= 1
print(f"Po dekrementaci: {counter}")

# -----------------------------------------------------------------------------
# Task 13: Comparing variables
# -----------------------------------------------------------------------------
num1: int = 25
num2: int = 15
result: bool = num1 > num2

print(f"Je {num1} větší než {num2}? {result}")

# -----------------------------------------------------------------------------
# Task 14: Age difference
# -----------------------------------------------------------------------------
father: int = 1974
child: int = 2007
difference: int = child - father

print(f"The father is {difference} years older than the child.")

# -----------------------------------------------------------------------------
# Task 15: Division
# -----------------------------------------------------------------------------
division_result: float = 11 / 7
rounded_result: float = round(division_result, 2)

print(f"11 : 7 = {rounded_result}")

# -----------------------------------------------------------------------------
# Task 16: User age (Anet, přidal jsem verifikaci, aby tam nešly zadat nesmysly). Data je lépe ošetřit na vstupu než opravovat dodatečně.

# -----------------------------------------------------------------------------
name: str = input("Zadejte jméno: ")

while True:
    year_str: str = input("Zadejte rok narození (YYYY): ")
    try:
        year: int = int(year_str)
        current_year: int = 2026

        if 1900 <= year <= current_year:
            age: int = current_year - year
            break
        else:
            print(f"Zadejte prosím reálný rok mezi 1900 a {current_year}.")
    except ValueError:
        print("Neplatný vstup! Zadejte prosím rok jako číslo (např. 1995).")

print(f"User: {name} is {age} years old.")
# ADHD nitpicking: Pokud je 15.5.2026 a dítě se narodilo 31.12.2025 má necelého půl roku. Šlo by ošetřit zadáním a odečtem na úrovní dní a měsíců pro now/birthday

# -----------------------------------------------------------------------------
# Task 17: While loop
# -----------------------------------------------------------------------------
i: int = 0
while i < 10:
    print("I'm a Pyth0n pr0gramm3r!")
    i += 1

# -----------------------------------------------------------------------------
# Task 18: Successive powers
# -----------------------------------------------------------------------------
for exponent in range(11):
    result: int = 2**exponent
    print(f"2^{exponent} = {result}")

# -----------------------------------------------------------------------------
# Task 19: Comparing names
# -----------------------------------------------------------------------------
first_name: str = input("Zadejte první jméno: ")
second_name: str = input("Zadejte druhé jméno: ")

if first_name == second_name:
    print("The same")
else:
    print("Different")
#  Malý hint pro Anet.  "o" nerovná se "ο". To první je latinské písmeno (U+006F), to druhé řecký omicron (U+03BF). Jsou to dva různé znaky i když vypadají stejně. (Homoglyphs)
#  Docela mne to kdysi potrápilo, protože používám obě klávesnice EN i GR :)

# -----------------------------------------------------------------------------
# Task 20: Comparing numbers
# -----------------------------------------------------------------------------
while True:
    try:
        a: float = float(input("Zadejte číslo a: "))
        b: float = float(input("Zadejte číslo b: "))
        break
    except ValueError:
        print("Chyba! Zadejte prosím číselné hodnoty.")

if a > b:
    print("a is greater!")
elif b > a:
    print("b is greater!")
else:
    print("a and b are equal!")
#  Opět včetně validace vstupů

# -----------------------------------------------------------------------------
# Task 21: Quadratic equations
# -----------------------------------------------------------------------------
print("The equation: a*x**2 + b*x + c == 0")

while True:
    try:
        a_coeff: float = float(input("Enter a: "))
        b_coeff: float = float(input("Enter b: "))
        c_coeff: float = float(input("Enter c: "))
        break
    except ValueError:
        print("Invalid input! Please enter numeric values.")

delta: float = b_coeff**2 - 4 * a_coeff * c_coeff

print("Primes of quadratic equation")
if delta > 0:
    x_1: float = (-b_coeff - delta**0.5) / (2 * a_coeff)
    x_2: float = (-b_coeff + delta**0.5) / (2 * a_coeff)
    print(f"x_1 = {x_1}")
    print(f"x_2 = {x_2}")
elif delta == 0:
    x_1: float = -b_coeff / (2 * a_coeff)
    print(f"x_1 = x_2 = {x_1}")
else:
    print("The delta is negative. No real roots.")
#  Opět včetně validace vstupů

# -----------------------------------------------------------------------------
# Task 22: Sum of numbers
# -----------------------------------------------------------------------------
while True:
    try:
        n: int = int(input("Enter a natural number n: "))
        if n >= 0:
            break
        print("Please enter a non-negative integer.")
    except ValueError:
        print("Invalid input! Please enter a number.")

# Way 1: Loop
loop_sum: int = 0
for i in range(n + 1):
    loop_sum += i
print(f"Sum using loop: {loop_sum}")

# Way 2: Python's built-in functions
builtin_sum: int = sum(range(n + 1))
print(f"Sum using sum() and range(): {builtin_sum}")
#  Opět včetně validace vstupů

# -----------------------------------------------------------------------------
# Task 23: Average
# -----------------------------------------------------------------------------
numbers: list[int] = [
    4,
    8,
    15,
    16,
    23,
    42,
]  # Zvolil jsem ikonická čísla ze seriálu Lost

total_sum: int = sum(numbers)
average: float = total_sum / len(numbers)

print(f"Entered numbers: {numbers}")
print(f"sum: {total_sum},")
print(f"average: {average}")

if total_sum > average:
    print("The sum is greater!")
elif average > total_sum:
    print("The average is greater!")
else:
    print("The sum and average are equal!")

# -----------------------------------------------------------------------------
# Task 24: Comparing strings
# -----------------------------------------------------------------------------
str1: str = "cat"
str2: str = "dog"

result: bool = str1 < str2

print(f"Is {str1} < {str2}? {result}")

# Comment: Python porovnává řetězce lexikograficky (podle abecedy/Unicode kódů).
# Protože 'c' má v tabulce nižší hodnotu než 'd', je 'cat' < 'dog' True.
# Je to stejné, jako když hledáme v encyklopedii nebo slovníku.
# Díky logiky Unicode jsou velká písmena řazena dříve (nižší value) než malá. Proto 'Python' > 'cobra' je True.


# -----------------------------------------------------------------------------
# Task 25: Defining list of numbers
# -----------------------------------------------------------------------------
even_numbers: list[int] = list(range(2, 99, 2))

for number in even_numbers:
    print(f"Number: {number}")


# -----------------------------------------------------------------------------
# Task 26: Multiplication table
# -----------------------------------------------------------------------------
while True:
    try:
        n: int = int(input("Give a number (1-10): "))
        if 1 <= n <= 10:
            break
        print("Please enter a number between 1 and 10.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

for i in range(1, 11):
    print(f"{i} * {n} = {i * n}")


# -----------------------------------------------------------------------------
# Task 27: FizzBuzz
# -----------------------------------------------------------------------------
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# -----------------------------------------------------------------------------
# Task 28: PEP 8 
# -----------------------------------------------------------------------------
#  Prohnal jsem to pomocí Ruff a sjednotil dle PEP 8