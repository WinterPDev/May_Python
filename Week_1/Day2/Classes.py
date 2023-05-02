'''

Objects exist in Python in a lot of existing things we've worked with. Such as why we can use some METHODS for certain things and not others.
For example: We can use .pop() on lists, but not on integers. Or that we can use .append() on lists and not dictionaries. 

This is an example of 'Encapsulation' which is one of the 'Four Pillars of OOP'. Which can be summarized as: 

Grouping our code together into objects and their appropriate methods for organization based on how we use those objects.

'''

#  Classes are how we build blueprints for objects. The parts of what make up these objects are called attributes.
# In addition to attributes that describe the object, we can also introduce methods. 
# Functions that perform actions associated with their object.


# Chel-sea Food Resturant

class Crab:
    
    # __init__ will intialize the constructor for our object!
    # This is where we put our blue print of attributes!
    # Classes need 'Constructors' that we create as a way to use our new blueprint to make an INSTANCE of an object.
    def __init__(self, Species, Buttered=True, Spiciness = 'Hot', Sides = ['Corn', 'Potatoes', 'Rice'], Quantity=4) -> None:
        self.Species = Species
        self.Buttered = Buttered
        self.Spiciness = Spiciness
        self.Sides = Sides
        self.Quantity = Quantity

    # self is an implicit parameter, so when we use self here it means we are giving the method the object it's being called with.
    def DisplayOrder(self):
        print(f'Species : {self.Species}\nButtered : {self.Buttered}\nSpiciness : {self.Spiciness}\nSides : {self.Sides}\nQuantity : {self.Quantity}\n============') # Species : 'King Crab'

# Butter, Spiciness, Sides, Species

CrabOrder1 = Crab('King Crab')
# print(CrabOrder1.Species)

CrabOrder1.DisplayOrder()

CrabOrder2 = Crab('King Crab', True, 'No Spice', ['Corn', 'Potatoes', 'Rice'], 8)

CrabOrder2.DisplayOrder()