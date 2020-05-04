import json
import os
import glob
from bookClasses import bookAd
from wrBooks import readingFromFile

def createFile(jsonFileName, data):
    with open(jsonFileName, 'w') as file:
        json.dump(data, file, indent=1)

def appendFile(databaseObj, dataObj):
    newDatabase = []
    for oneBookAd in databaseObj.getData():
        newDatabase.append(oneBookAd)
    for oneBookAd in dataObj.getData():
        newDatabase.append(oneBookAd)

    databaseFile = databaseObj.getFileName()
    os.remove(databaseFile)
    createFile(databaseFile, newDatabase)

def save(jsonFileName, data):
    os.remove(jsonFileName)
    with open(jsonFileName, 'w') as file:
        json.dump(data, file, indent=1)
    