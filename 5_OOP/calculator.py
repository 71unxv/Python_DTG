import os

class Calculator() :

    def __init__(self, value_1, value_2) :
        self.value_1 = float(value_1)
        self.value_2 = float(value_2)
        self.remain = 0
    
class Count(Calculator) :
    def Add(self) :
        self.result = self.value_1 + self.value_2 
        return self.result
    
    def Substract(self) :
        self.result = self.value_1 - self.value_2 
        return self.result
        
    def Multiply(self) :
        self.result = self.value_1 * self.value_2 
        return self.result
    
    def Intersect(self) :
        self.result = self.value_1 // self.value_2 
        return self.result
    
    def changeRemain(self):
        self.remain = self.result
        return self.remain

def RunCalculator() :
    status = True
    while status :
        os.system('clear')
        print("*************** Calculator OOP **********************")
        value_1 = input("Please input the number 1 : ")
        value_2 = input("Please input the number 2 : ")
        calculator = Count(value_1,value_2)
        print("*****************************************************")
        print("Please choose the action below :")
        print("1. Add the number ")
        print("2. Substract the number")
        print("3. Multiply the number")
        print("4. Intersect the number")
        choice = input("your choice :")
        if choice == 1 :
            display = calculator.Add()
            store_number = calculator.changeRemain()
            print("The result is : ", display)
        elif choice == 2 :
            display = calculator.Substract()
            store_number = calculator.changeRemain()
        elif choice == 3 :
            display = calculator.Multiply()
            store_number = calculator.changeRemain()
        elif choice == 4 :
            display = calculator.Intersect()
            store_number = calculator.changeRemain()
        
        break

        


if __name__ == "__main__" :
    RunCalculator()