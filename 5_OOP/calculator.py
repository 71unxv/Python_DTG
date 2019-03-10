import os

class Calculator() :

    def __init__(self, value_1, value_2) :
        self.value_1 = float(value_1)
        self.value_2 = float(value_2)
        self.remain = 0
    
    def askChoice(self, value) :
        if value == 1 :
            self.value_1 = self.remain
            self.value_2 = int(input("Please insert your number : " ))
            print("Please choose the action below :")
            print("1. Add the number ")
            print("2. Substract the number")
            print("3. Multiply the number")
            print("4. Intersect the number")
            choice = int(input("your choice :"))
            return choice
        elif value == 2 :
            choice = "None"
            return choice
    
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
    C = True
    while status :
        os.system('clear')
        C = True
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
        choice = int(input("your choice :"))
        while C :
            if choice == 1 :
                display = calculator.Add()
                calculator.changeRemain()
                print("The result is : ", display)
                print("*****************************************************")
                print("1. Calculate with the result (C) ")
                print("2. Calculate with new number (C) ")
                cmd = int(input("What do you want to do next ? "))
                choice = calculator.askChoice(cmd)
                if choice == "None" :
                    C = False
            elif choice == 2 :
                display = calculator.Substract()
                calculator.changeRemain()
                print("The result is : ", display)
                print("*****************************************************")
                print("1. Calculate with the result (C) ")
                print("2. Calculate with new number (C) ")
                cmd = int(input("What do you want to do next ? "))
                choice = calculator.askChoice(cmd)
                if choice == "None" :
                    C = False
            elif choice == 3 :
                display = calculator.Multiply()
                calculator.changeRemain()
                print("The result is : ", display)
                print("*****************************************************")
                print("1. Calculate with the result (C) ")
                print("2. Calculate with new number (C) ")
                cmd = int(input("What do you want to do next ? "))
                choice = calculator.askChoice(cmd)
                if choice == "None" :
                    C = False
            elif choice == 4 :
                display = calculator.Intersect()
                calculator.changeRemain()
                print("The result is : ", display)
                print("*****************************************************")
                print("1. Calculate with the result (C) ")
                print("2. Calculate with new number (C) ")
                cmd = int(input("What do you want to do next ? "))
                choice = calculator.askChoice(cmd)
                if choice == "None" :
                    C = False
if __name__ == "__main__" :
    RunCalculator()