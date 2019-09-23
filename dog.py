# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print( self.name + " Woof!")
    def sit(self):
        print( self.name + " sits!")
    def rollover(self):
        print( self.name + " rolls over!")
# print(my_dog) #the instance is call my_dog
# print(my_dog.breed)# the property of the instance called instance variable
