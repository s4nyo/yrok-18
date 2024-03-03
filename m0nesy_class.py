class Class:
    def __init__(self, size, number):
        self.size = size
        self.number = number

    def tarakan(self):
        print(self.size, self.number)

our = Class('60м^3', '10')
informatika = Class('50м^3', '312')

our.tarakan()
informatika.tarakan()