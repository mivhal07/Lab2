list = []

count = 0
while count < 10:
    a = int(input("Wprowadź liczbę: "))
    result = a % 2
    if (result == 0):
        list.append(a)
    count += 1
print(list)
