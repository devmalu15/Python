class Bird:
    def fly(self):
        print("It is little and flies")
                                                    #Both Bird and Dinosaur classes have fly() method
class Dinosaur:
    def fly(self):
        print("It is very big and flies")

class Flying:
    def canFly(self, animal):                       #Here animal can be any object thats class has fly() method
        animal.fly()                                

eagle = Bird()                                       
pteranodon = Dinosaur()


flying = Flying()
                                                    #If two or more things have fly() method then they are treated equally and can be passed in a method which asks for this argument. This is possible with the help of Duck Typing.
flying.canFly(eagle)
flying.canFly(pteranodon)