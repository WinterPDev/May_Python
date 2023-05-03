# Importing across files in Python
from rpg_classes.Player import Player

class Warrior(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.strength += 10
        self.hp += 20
        self.defense += 5


    def Warrior_Rage(self, target):
        target.defend(self.strength*2)
        self.defend(self.strength)
        print(f'{self.name} attacks wrecklessly!')
        print(f'{target.name} now has {target.hp}.')
        print(f'{self.name} took recoil damage! Now has {self.hp}')