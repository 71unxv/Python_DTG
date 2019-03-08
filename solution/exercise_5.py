def isPrime(number) :
    zero_mod = []
    if number == 1 :
        return False
    else :
        for divider in range(1,number+1) :
            remain = number % divider
            if remain == 0 :
                zero_mod.append(divider)
    
    if len(zero_mod) == 2 :
        return True
    else :
        return False

def PrintPrime(list_number):
    for number in list_number :
        if isPrime(number) == True :
            print(f"The {number} is a prime number")
        elif isPrime(number) == False :
            print(f" The {number} is not a prime number")

PrintPrime([2])
PrintPrime([3])
PrintPrime([1,2,3,4,5])
