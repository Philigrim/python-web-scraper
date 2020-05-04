class Seller:

    def __init__(self, username, city):
        self.username = username
        self.city = city

    def getUsername(self):
        return self.username
    def getCity(self):
        return self.city
    def getSellerInfo(self):
        return {'username' : self.username,
                'city' : self.city}

    def changeUsername(self, username):
        self.username = username
    def changeCity(self, city):
        self.city = city
    def changeSellerInfo(self, username, city):
        self.username = username
        self.city = city

    @staticmethod 
    def getDifferentRecords(users, record):
        diffRecords = []
        if record.lower() == "username":
            for user in users:
                diffRecords.append(user.getUsername())
        elif record.lower() == "city":
            for user in users:
                if(user.getCity() != "Nenurodyta"):
                    diffRecords.append(user.getCity())
        else:
            return "Wrong record."
        return set(diffRecords)

    @staticmethod 
    def getSellerCountByCity(users, city):
        count = 0
        for user in users:
            if user.getCity().lower() == city.lower():
                count += 1
        return count       
        
    @staticmethod 
    def getSellerUsernamesByCity(users, city):
        usersByRecord=[]
        for user in users:
            if user.getCity().lower() == city.lower():
                usersByRecord.append(user.getUsername())
        return usersByRecord