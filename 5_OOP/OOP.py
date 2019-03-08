class Bird():
    def __init__(self) :
        self.wings = True
        self.fur = True
        self.fly = True
    
    def isFly(self) :
        return self.fly

Parrot = Bird()

if Parrot.isFly() == "fly" :
    print("Parrot must be can fly")
else :
    print("Why Parrot can't fly ?")


###### Inheritance #####
class Penguin(Bird) :
    def __init__(self) :
        self.fly = False

Penguin = Penguin()

if Penguin.isFly() == True :
    print("No way, penguin can't fly")
else :
    print("Penguin is swimming")
    ######################