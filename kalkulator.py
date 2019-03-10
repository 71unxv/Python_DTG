""" Created on : Sun Mar 10 18:26:25 2019
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

import os

# Function
#   ==============================================================================================================


# run code! Run!!
#   ==============================================================================================================
def kalkulator():
    def __init__(self,nomor):
        self.nomor = nomor
        return self.nomor
    def tambah(self,nomorbaru):
        self.nomor = self.nomor+nomorbaru
        return self.nomor
    def kurang(self,nomorbaru):
        self.nomor = self.nomor - nomorbaru
        return self.nomor
    def bagi(self,nomorbaru):
        self.nomor = self.nomor/nomorbaru
        return self.nomor
    def kali(self,nomorbaru):
        self.nomor = self.nomor+nomorbaru
        return self.nomor
    def modulo(self,nomorbaru):
        self.nomor = self.nomor % nomorbaru
        return self.nomor


clear = lambda: os.system('cls')

stopcriteria = False
first = True
while stopcriteria == False:
    clear()
    print("=" * 20)
    print((" "*10 )+ "Jiunx Calc")
    print("..")
    print("..")
    if first:
        print("please input your number")
        nomor = input()
        print("Current Number:")
        print(nomor)
        print("..")
    else:
        print("please input your commands:")
        print("1 for add ")
        print("2 for substract ")
        print("3 for divide ")
        print("4 for multiply ")
        
        command = int(input("please input your commands:"))
        if command == 1:
            temp = input("please input your number")
            nomor = kalkulator.tambah(temp)
        elif command == 2:
            temp = input("please input your number")
            nomor = kalkulator.kurang(temp)
        elif command == 3:
            temp = input("please input your number")
            nomor = kalkulator.bagi(temp)
        elif command == 4:
            temp = input("please input your number")
            nomor = kalkulator.kali(temp)
        
        
