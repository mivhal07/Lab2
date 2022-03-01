a = int(input("Wprowadź pierwszą liczbę całkowitą: "))
b = int(input("Wprowadź drugą liczbę całkowitą: "))
c = int(input("Wprowadź trzecią liczbę całkowitą: "))

if (a > b) & (a > c):
    if (b > c):
        print("Kolejność malejąco to: " + str(a) + " " + str(b) + " " + str(c))
    else:
        print("Kolejność malejąco to: " + str(a) + " " + str(c) + " " + str(b))
if (b > a) & (b > c):
    if (a > c):
        print("Kolejność malejąco to: " + str(b) + " " + str(a) + " " + str(c))
    else:
        print("Kolejność malejąco to: " + str(b) + " " + str(c) + " " + str(a))
if (c > a) & (c > b):
    if (a > b):
        print("Kolejność malejąco to: " + str(c) + " " + str(a) + " " + str(b))
    else:
        print("Kolejność malejąco to: " + str(c) + " " + str(b) + " " + str(a))
