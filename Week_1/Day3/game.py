'''
Objective : Build out a basic set of RPG classes and have them combat each other.

Incorporating OOP we will use:
- Encapsulation - The individual classes will be grouped and organized accordingly.
- Inheritance - Construct a Player/Human class to build the other RPG classes off of to avoid repetition.
- Polymorphism - Some methods can share the same name across child classes, but they operate differently based on that class.
- Abstraction - Related to Encapsulation, other classes will be able to operate without requiring access/know the other class' information to execute.
'''
from rpg_classes.Warrior import Warrior
from rpg_classes.Wizard import Wizard
import random

warrior = Warrior('Conan')
wizard = Wizard('Merlin')

# NOTE: RUN THIS THIS CODE IN A TERMINAL FOR INPUTS! 🐍

print(f'The warrior: {warrior.name} approaches the wizard: {wizard.name}!')

while warrior.hp > 0 and wizard.hp > 0:
    player_input = ""
    while not player_input == "1" and not player_input == "2":
        player_input = input("What to do?\n 1) Attack\n 2) Use skill\n <=========>")
        if player_input == "1":
            warrior.attack(wizard)
        elif player_input == "2":
            warrior.Warrior_Rage(wizard)
        else:
            print("Choose a valid option! (1 or 2)")
        
    coin_toss = random.randint(1,2)
    if coin_toss == 1:
        wizard.attack(warrior)
    else:
        wizard.magearmor()

    if warrior.hp > 0:
        print("You win!")
    elif wizard.hp <= 0:
        print("Draw!")
    else:
        print("The Wizard Wins!")
        