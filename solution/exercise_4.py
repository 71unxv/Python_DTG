numbers = []
for i in range(1,101) :
    numbers.append(i)

prime_number = []
for number in numbers :
    zero_mod = []
    if number == 1 :
        continue
    else :
        for divider in range(1,number+1) :
            remain = number % divider
            if remain == 0 :
                zero_mod.append(divider)
    
    if len(zero_mod) == 2 :
        prime_number.append(number)

print(prime_number)

