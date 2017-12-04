import datetime

#static method
class DummyUtils:
    @staticmethod
    def dummy():
        print("Dummy method")

DummyUtils.dummy()

class Car:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year
        Car._year = year
        Car._brand = brand

    def getInfo(self):
        print("year: {}, brand: {}".format(self._year, self._brand))

    @classmethod
    def getAge(cls):
        now = datetime.datetime.now()
        return int(now.year) - cls._year


car1 = Car("BMW", 2010)

car1.getInfo()

car2 = Car("Benz", 2008)

Car.getInfo(car2)

print(car1.getAge())

print(car2.getAge())





