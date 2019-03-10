def PrintPrime(numbers : list) :
    for number in numbers :
        factor = 0
        for divider in range(1,number+1) :
            if number % divider == 0 :
                factor += 1
        
        if factor == 2 :
            print(f"The {number} is a prime number")
        else :
            print(f"The {number} is not a prime number")




numbers = []
for i in range (1,1001) :
    numbers.append(i)

PrintPrime(numbers)