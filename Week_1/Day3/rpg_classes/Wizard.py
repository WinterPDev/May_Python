from rpg_classes.Player import Player


class Wizard(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.strength -= 5
        self.mana = 30
        self.defense = 5


    def attack(self, target):
        # super().attack(target) # an example of using an inherited method instead of repeating.
        print(f'{self.name} casts Fireball at {target.name}!')
        target.defend(self.mana)

    def mageArmor(self):
        print(f'{self.name} increases their defense by {self.mana/2}!')
        self.defense += self.mana/2
        print(f'{self.name} now has {self.defense} armor!')