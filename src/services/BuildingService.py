from src.services.FileService import *
from src.entities.Building import *
from src.entities.Apartment import *

# Get all buildings from data files
def getAllBuildings() -> list[Building]:
    data: list[list[str]] = getDataFromFiles()
    return getBuildingsFromData(data)

# Get buildings from field value
def getBuildingsByField(fieldIndex: int, value: str) -> list[Building]:
    def filterByFieldValue(x: list[str]) -> bool:
        return x[fieldIndex].lower() == value.lower()

    data: list[list[str]] = getDataFromFiles()
    filteredData = filter(filterByFieldValue, data)

    return getBuildingsFromData(filteredData)

# Get building entities from extracted data
def getBuildingsFromData(data: list[list[str]]) -> list[Building]:
    buildings: list[Building] = []
    i: int = 0
    for d in data:
        newApartment: Apartment = Apartment(d[0], d[2], d[6], d[7],d[8])
        if len(buildings) > 0 and d[1] == buildings[i-1].getBuildingId():
            buildings[i-1].addApartment(newApartment)
        else:
            newBuilding: Building = Building(d[1], d[3], d[4], d[5])
            newBuilding.addApartment(newApartment)
            buildings.append(newBuilding)
            i+=1

    return buildings

# Display buildings in params
def printBuildings(buildings: list[Building]) -> None:
    print("{:<10} {:<15}".format('ID imm','Adresse'))
    for b in buildings:
        b.print()
