# Chel-sea Food Resturant

class Crab:

    def __init__(self, Species, Buttered=True, Spiciness = 'Hot', Sides = ['Corn', 'Potatoes', 'Rice'], Quantity=4) -> None:
        self.Species = Species
        self.Buttered = Buttered
        self.Spiciness = Spiciness
        self.Sides = Sides
        self.Quantity = Quantity
        # Inside the class of Crab, append the created Crab to the List after it's made.

    def DisplayOrder(self):
        print(f'Species : {self.Species}\nButtered : {self.Buttered}\nSpiciness : {self.Spiciness}\nSides : {self.Sides}\nQuantity : {self.Quantity}\n============')
        return self

CrabOrder1 = Crab('King Crab')
CrabOrder2 = Crab('King Crab', True, 'No Spice', ['Corn', 'Potatoes', 'Rice'], 8)

# CrabOrder1.DisplayOrder()

# Crab.Get_Orders()


class Customer:
    All_Customers = []
    def __init__(self, Name, Ticket_Number, Payment) -> None:
        self.Name = Name
        self.Ticket_Number = Ticket_Number
        self.Payment = Payment
        self.Order = Crab('King Crab')
        self.Served = False
        Customer.All_Customers.append(self)

    @classmethod
    def Get_Orders(cls):
        for customer in cls.All_Customers:
            print(f'Customer Name : {customer.Name}')
            customer.Order.DisplayOrder()

    def OrderReceipt(self):
        Customer.ServeOrder(self)
        print(f'Name : {self.Name}')
        self.Order.DisplayOrder()
        return self
    
    @staticmethod
    def ServeOrder(customer):

        if customer.Served == False:
            customer.Served = True
            print('Customer is now Served!')
        else:
            print('Customer Already Served!')

Customer1 = Customer('Gary', 1, 'The Black Crab Card')

# Customer1.OrderReceipt()

Customer1.OrderReceipt()
Customer1.OrderReceipt()