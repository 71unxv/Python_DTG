class ChangeNumber() :
    def __init__(self,number) :
        self.number = number
    
    def change(self, number):
        self.number = number
    
    def double(self) :
        double = self.number * self.number
        self.change(double)

    def printNumber(self) :
        print("Now the number is ", self.number)

""" Sequential Programming """
#1. Create Number
number = 10
print("Now the number is ", number)
#2. Change Number
number = 5
print("Now the number is ", number)
#3. Double the number
number = number * number
print("Now the number is ", number)
""" ---------------------------- """

""" OOP Programming  """
# Assume we have make a class
#1. Instaniate Object
number = ChangeNumber(10)
number.printNumber()

#2. Change Number
number.change(5)
number.printNumber()

#3. Double the Number
number.double()
number.printNumber()
""" ---------------------------- """


