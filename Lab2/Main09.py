import math

a = int(input('Wprowadź liczbę całkowitą: '))
try:
    result = math.sqrt(a)
    print('Pierwiastek z tego liczby to: ' + str(result))
except Exception:
    print('Nie mogę spierwiastkować liczby mniejszej niż 0')
