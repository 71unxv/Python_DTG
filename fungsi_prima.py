""" Created on : Sun Mar 10 15:16:46 2019
    author: 
        github.com/71unxv
        github.com/LutfiZakaria
        
    Note:
    
     Python for Geophysical Data Processing and Inverse Problem  
    _______________________________________________________________________________

    Cheers!
"""
# Import Library
#   ==============================================================================================================


# Function
#   ==============================================================================================================
def isPrime(x):
#    stop = False
    count = 0
    isprima = True
    fac_num = 0
    while count<=10:
        
        count += 1
        if x % count == 0:
            fac_num += 1
            if (fac_num > 2) :
                isprima = False
                return isprima
                    
    if x == 1:
        isprima = False
    return isprima

def listPrime(x):
    for ii in range(len(x)):
        if isPrime(x[ii]):
            print(str(x[ii]) + " is Prime")
        else :
            print(str(x[ii]) + " is not Prime")

a = 1
print(isPrime(a))
a = 4
print(isPrime(5))

import numpy as np
a = np.arange(1,20)
listPrime(a)
            
# run code! Run!!
#   ==============================================================================================================




