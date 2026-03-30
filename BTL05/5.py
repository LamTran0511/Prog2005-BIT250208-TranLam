class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def __str__(self):
        return f'Ten hoa la: {self.name}, mau sac:  {self.color}'
hoa_first = Flower('hoa', 'red')