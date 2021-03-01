class Warehouse:
    sector_a = 'OfficeEquipment'
    sector_b = 'Station'


class OfficeEquipment(Warehouse):

    def __init__(self, name, price, year):
        self.name = name
        self.price = price
        self.year = year
