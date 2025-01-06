class Burger:
    def __init__(self, bun=None, lettuce=None, patty=None, cheese=None):
        self.bun = bun
        self.lettuce = lettuce
        self.patty = patty
        self.cheese = cheese

    def american_burger(self, **toppings):
        self.bun = "White"
        self.lettuce = "Contains"
        self.patty = "Beef"
        self.cheese = "American"
        price = 20.00
        for key, value in toppings.items():
            price += 2.00
        return f"American Burger: {self.bun} bun, {self.lettuce} lettuce, {self.patty} patty, and {self.cheese} cheese with {toppings}\nThe total price is: ${price:.2f}"

    def australian_burger(self, **toppings):
        self.bun = "Black"
        self.lettuce = "No"
        self.patty = "Beef"
        self.cheese = "Cheddar"
        price = 30.00
        for key, value in toppings.items():
            price += 2.00
        return f"Australian Burger: {self.bun} bun, {self.lettuce} lettuce, {self.patty} patty, and {self.cheese} cheese with {toppings}\nThe total price is: ${price:.2f}"

    def brazilian_burger(self, **toppings):
        self.bun = "French"
        self.lettuce = "Contains"
        self.patty = "Beef"
        self.cheese = "Mozzarella"
        price = 25.00
        for key, value in toppings.items():
            price += 2.00
        return f"Brazilian Burger: {self.bun} bun, {self.lettuce} lettuce, {self.patty} patty, and {self.cheese} cheese with {toppings}\nThe total price is: ${price:.2f}"

    def louisiana(self, **toppings):
        self.bun = "White"
        self.lettuce = "Contains"
        self.patty = "Chicken"
        self.cheese = "American"
        price = 26.00
        for key, value in toppings.items():
            price += 2.00
        return f"Louisiana Burger: {self.bun} bun, {self.lettuce} lettuce, {self.patty} patty, and {self.cheese} cheese with {toppings}\nThe total price is: ${price:.2f}"

if __name__ == '__main__':
    burger_order = Burger()
    print(burger_order.american_burger(bacon=True, pickles=False, double=False))
    print(burger_order.louisiana(bacon=True, pickles=False, barbecue=True, double=False))