class Buildibg:
    year = None
    city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print('Year:', self.year, '. City', self.city)

class School(Buildibg):
    pupils = 0

    def __init__(self, pupils, year, city):
        super(School, self).__init__(year, city)
        self.pupils = pupils

    def get_info(self):
        super().get_info()
        print('Pupils:', self.pupils)

class House(Buildibg):
    pass

class Shop(Buildibg):
    pass

school = School(100, 2000, 'Mocs')
school.get_info()