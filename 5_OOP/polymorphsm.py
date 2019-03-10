class PhysicsForce :
    class PhysicsGG :
        pass
    
    def W(self, Force, Distance) :
        usaha = Force * Distance
        return usaha

class PhysicsRotation :
    def W(self, frequency) :
        omega = 2 * 3.15 * frequency
        return omega

Rinta = PhysicsForce()
Usaha = Rinta.W(3,2)
print(Usaha)
Marsa = PhysicsRotation()
Omega = Marsa.W(4)
print(Omega)




# class Parrot:
#     def fly(self):
#         print("Parrot can fly")
    
#     def swim(self):
#         print("Parrot can't swim")

# class Penguin:
#     def fly(self):
#         print("Penguin can't fly")
    
#     def swim(self):
#         print("Penguin can swim")

# # common interface
# def flying_test(bird):
#     bird.fly()

# #instantiate objects
# blu = Parrot()
# peggy = Penguin()

# # passing the object
# flying_test(blu)
# flying_test(peggy)