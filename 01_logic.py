class Bill:
    def __init__(self):
        self.money = 0
    def add(self, count):
        self.money += count
    def buy(self, count, name):
        pass


leo_bill = Bill()
print(leo_bill.money)

leo_bill.add(10)
leo_bill.add(20)

print(leo_bill.money)

kate_bill = Bill()
print(kate_bill.money)

kate_bill.add(1)
print(kate_bill.money)

print('А у Лео осталось 30, так как это другой объект', leo_bill.money)
