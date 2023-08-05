
import random
class Bot:
    def __init__(self, name):
        self.Name = name
        self.Health = 100
        self.BaseArmor = 10
        self.BaseDamage = 10
        self.Speed = 10
    def attack(self, opponent):
        damage_dealt = self.BaseDamage - (self.BaseDamage * opponent.BaseArmor() / 100)
        opponent.take_damage(damage_dealt)

    def takeDamage(self, DamageAmount):
        self.Health -= DamageAmount

    def BuildAttack(self):
        self.Speed -= 2
        self.BaseArmor -= 2
        self.BaseDamage += 2

    def BuildSpeed(self):
        self.Speed += 2
        self.BaseArmor -= 2
        self.BaseDamage -= 2

    def BuildArmor(self):
        self.Speed -= 2
        self.BaseArmor += 2
        self.BaseDamage -= 2

    def IsAlive(self):
        if self.Health > 0:
            return True
        else:
            return False

    def Get_Stats(self):
        print("Name: " + str(self.Name))
        print("Name: " + str(self.Name))
        print(self.BaseArmor)
        print(self.Speed)
        print(self.Health)

    def action(self, opponent):
        RandomNumber = random.randint(0, 100)
        if RandomNumber <= 20:
            self.build_armor()
        elif RandomNumber <= 40:
            self.build_attack()
        elif RandomNumber <= 60:
            self.build_speed()
        elif RandomNumber <= 90:
            self.attack(opponent)
        else:
            print(self.name + " glitched out!")