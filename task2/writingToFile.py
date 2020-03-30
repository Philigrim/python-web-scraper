import json
import os
import bookAd

class Writing:
    filename = ""
    data = []

    def __init__(self, filename, data):
        self.filename = filename
        self.data = data

    def save(self, datatype, state):
        if state == "change":
            if os.path.exists(self.filename):
                os.remove(self.filename)
        if datatype.lower() == "bookads":
            if os.path.exists(self.filename):
                with open(self.filename, "a") as self.saveFile:
                    for dataLine in self.data:
                        self.saveFile.write("\n" + json.dumps(bookAd.BookAd.getBookAdInfo(dataLine)))
            else:    
                with open(self.filename, "w") as self.saveFile:
                    for dataLine in self.data:
                        self.saveFile.write(json.dumps(bookAd.BookAd.getBookAdInfo(dataLine)) + "\n")
        else:
            if os.path.exists(self.filename):
                with open(self.filename, "a") as self.saveFile:
                    for dataLine in self.data:
                        self.saveFile.write("\n" + json.dumps(dataLine.__dict__))
            else:    
                with open(self.filename, "w") as self.saveFile:
                    for dataLine in self.data:
                        self.saveFile.write(json.dumps(dataLine.__dict__) + "\n")
    
