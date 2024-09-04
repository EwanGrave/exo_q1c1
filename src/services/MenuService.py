from src.services.BuildingService import *
from src.entities.Building import *

# Display menu to user
def getMenu() -> None:
    # Get user choice from a set of possible values
    def getUserChoice(msg: str, list: list[int]) -> int:
        choice: int = int(input(msg))
        while choice not in list:
            choice = int(input(msg))
        return choice

    choice: int = getUserChoice("Choisissez : (0) Quitter | (1) Afficher tous les immeubles | (2) Rechercher sur colonne\n", [0, 1, 2])

    # display all buildings
    if choice == 1:
        printBuildings(getAllBuildings())

    # display buildings from a request
    if choice == 2:
        fieldIndex: int = getUserChoice('(0) property | (1) building_id | (2) owner_acquisition_date | (3) street1 | (4) city | (5) zip | (6) lastname | (7) firstname | (8) email : ',
                                        [0, 1, 2, 3, 4, 5, 6, 7, 8])
        value: str = input('Valeur : ')
        buildings: list[Building] = getBuildingsByField(int(fieldIndex), value)
        printBuildings(buildings)

    # Continue if user not quitting
    if choice != 0:
        getMenu()
