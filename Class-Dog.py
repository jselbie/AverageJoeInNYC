from Class import Pet
class Dog(Pet):
    def __init__(self, name, volume):
        super(). __init__(name)
        self.volume = volume


    def Bark(self):
        if self.volume > 3:
            print("woof woof woof")
        else:
            print("yip yip yip")
Small_dog = Dog("Pup", 2)
Big_dog = Dog("Coco", 5)

Small_dog.Bark()
Big_dog.Bark()
