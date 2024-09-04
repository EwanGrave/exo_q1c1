# Apartement entity class
class Apartment:
    def __init__(self, property, owner_acquisition_date, lastname, firstname, email):
        self.property = property
        self.owner_acquisition_date = owner_acquisition_date
        self.lastname = lastname
        self.firstname = firstname
        self.email = email

    def getProperty(self):
        return self.property

    def getOwnerAcquisitionDate(self):
        return self.property

    def getLastname(self):
        return self.lastname

    def getFirstname(self):
        return self.firstname

    def getEmail(self):
        return self.email
    
    def print(self):
        print("{:<10} {:<12} {:<40} {:<15}".format(self.property, self.owner_acquisition_date, self.firstname + ' ' + self.lastname, self.email))
