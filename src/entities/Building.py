from src.entities.Apartment import *

# Building entity class
class Building:
    def __init__(self, building_id, street1, city, zip):
        self.building_id = building_id
        self.street1 = street1
        self.city = city
        self.zip = zip
        self.apartments: list[Apartment] = []
    
    def getBuildingId(self):
        return self.building_id

    def getStreet1(self):
        return self.street1

    def getCity(self):
        return self.city

    def getZip(self):
        return self.zip

    def addApartment(self, apartment):
        self.apartments.append(apartment)

    def print(self):
        print("{:<10} {:<15}".format(self.building_id, self.street1 + ' ' + self.city + ' ' + self.zip))
        print('--------------------------------------------------------------------------------------')
        print("{:<10} {:<12} {:<40} {:<15}".format('ID appart', 'Date', 'Propriétaire', 'Email'))
        for a in self.apartments:
            a.print()
        print()
