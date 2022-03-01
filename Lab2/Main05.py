a = int(input("Wprowadź pierwszą liczbę całkowitą: "))
b = int(input("Wprowadź drugą liczbę całkowitą: "))
c = int(input("Wprowadź trzecią liczbę całkowitą: "))

result = str(pow(a, b) + c)

# pojęcia nie mam jak użyć tego readline()
f = open('demoFile.txt', 'w')
f.write(result)
f.close()
