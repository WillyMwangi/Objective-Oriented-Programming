# Factories need to maintain a specific level of stock as well as avoid overstocking or stock deficits

# this program helps the factory manage stocks in an easy way.
class factoryStock():
    def inventory():
        pass

class PremiumGoods(factoryStock): # Premium goods inherits from factory stock
    def __init__(self):
        self.balance = 1000

    def inventory(self, inventory):
        if type(inventory) == int and inventory != "":
            if inventory >= 0:
                self.balance += inventory
                return self.balance

            else:
                return 'Invalid Stock'

        else:
            raise ValueError()

    def orders(self, stock):
        if type(stock) == int and stock != "":
            if stock > 0:
                if (self.balance - stock) > 0:
                    if (self.balance - stock) > 1000:
                        self.balance -= stock
                        return self.balance
                    else:
                        return 'Insufficient Stock in Factory'
                else:
                    return 'Enter Stock below Actual balance'
            else:
                return 'Invalid Stock'
        else:
            raise ValueError()


class stockLevel(factoryStock): # stock levels inherit from factoryStock
    def __init__(self):
        self.balance = 0

    def inventory(self, inventory):
        if type(inventory) == int and inventory != "":
            if inventory >= 0:
                self.balance += inventory
                return self.balance

            else:
                return 'Invalid inventory stock'

        else:
            raise ValueError()

    def orders(self, stock):
        if type(stock) == int and stock != "":
            if stock > 0:
                if (self.balance - stock) > 0:

                    self.balance -= stock
                    return self.balance

                else:
                    return 'Enter Stock below Actual balance'
            else:
                return 'Invalid order of Stock'
        else:
            raise ValueError()

