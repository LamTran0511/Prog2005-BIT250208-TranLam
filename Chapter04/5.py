class Product:
    def __init__(self, price):
        self._price = None
        self.price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError('Gia phai > 0')
    def __str__(self):
        return f'Gia SP: {self._price}'

a = Product(20)
print(a)