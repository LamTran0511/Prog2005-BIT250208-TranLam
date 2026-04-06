class Book:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @name.setter
    def name(self, name):
        self._name = name

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price phải >= 0")
        self._price = price


n = Book('truyen ma', 50000)

print(n.name)
print(n.price)

n.price = 60000
print(n.price)