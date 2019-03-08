numbers = []
for i in range (1,22) :
    numbers.append(i)

for number in numbers :
    if number % 2 == 0 :
        print("Genap")
    elif number % 2 == 1 :
        print("Ganjil")