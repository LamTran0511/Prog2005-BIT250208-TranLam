class Book:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    def get_name(self):
        return self._name
    def get_price(self):
        return self._price
    def set_name(self, name):
        self._name = name
    def set_price(self, price):
        self._price = price
n = Book('truyen ma', 50000)
print(n.get_name())
print(n.get_price())