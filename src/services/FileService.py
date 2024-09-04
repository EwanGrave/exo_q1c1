from os import listdir
from operator import itemgetter
import csv

# Get all data sorted from data files.
def getDataFromFiles() -> list[list[str]]:
    baseFolder: str = 'data/'
    fileList: list[str] = listdir(baseFolder)
    data: list[list[str]] = []

    # parse all files in data folder
    for file in fileList:
        with open(baseFolder+file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader, None)
            for row in reader:
                if len(row) != 0 :
                    data.append(row)
    
    # Sorted by building id and owner name
    sortedData: list[list[str]] = sorted(data, key=itemgetter(1, 6, 7))
    return sortedData
