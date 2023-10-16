class Item:
    # This is a class attribute
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int):

        # Run validations for the received arguments
        assert price >= 0, f"{price} is not greater than 0!!!"
        assert quantity >= 0, f"{quantity} is not greater than 0!!!"

        # Assign parameter values into self object. These are basically instance attributes.
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to perform
        Item.all.append(self)

    # Represent an object

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"""Item name is {self.name} and it's price is {self.price} 
                    and we have {self.quantity} number of items in our store.
                """
    def calculate_prices(self):
        print(f"Total item price is {self.quantity * self.price}")

    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("Mobile", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

# It's not like to add an attribute, we only have to pass attributes into constructors.
# We can easily do it by this way.

item2.has_numpad = False

# Accessing class attributes
print(Item.pay_rate)
print(item1.pay_rate)

# To get information to access all the attributes from class/instance level,
# we can use magic methods
print(Item.__dict__)
print(item1.__dict__)

item1.apply_discount()
item2.pay_rate = 0.5
item2.apply_discount()
print(item1.price)
print(item2.price)

print(Item.all)