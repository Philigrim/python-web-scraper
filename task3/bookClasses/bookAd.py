import json

class BookAd:

    def __init__(self, bookObj, sellerObj, price, condition, comment):
        self.bookObj = bookObj
        self.sellerObj = sellerObj
        self.price = price
        self.condition = condition
        self.comment = comment

    def getBook(self):
        return self.bookObj
    def getSeller(self):
        return self.sellerObj
    def getPrice(self):
        return self.price
    def getCondition(self):
        return self.condition
    def getComment(self):
        return self.comment
    def getBookAdInfo(self):
        BookAdInfo = self.bookObj.getBookInfo()
        BookAdInfo.update(self.sellerObj.getSellerInfo())
        BookAdInfo.update(price = self.price, condition = self.condition, comment = self.comment)
        return BookAdInfo

    def changePrice(self, price):
        self.price = price
    def changeCondition(self, condition):
        self.condition = condition
    def changeComment(self, comment):
        self.comment = comment
    def changeBookInfo(self, bookObj, seller, price, condition, comment):
        self.bookObj = bookObj
        self.sellerObj = seller
        self.price = price
        self.condition = condition
        self.comment = comment

    @staticmethod 
    def getRecordsByRecordType(bookAds, record):
        diffRecords = []
        if (record.lower() == "title" or (record.lower() == "author") or (record.lower() == "releasedate") or (record.lower() == "category")):
            for bookAd in bookAds:
                diffRecords.append(getattr(bookAd.getBook(), record))
        elif record.lower() == "genre":
            for bookAd in bookAds:
                diffRecords.append(bookAd.getBook().getBookType())
        elif (record.lower() == "username") or (record.lower() == "city"):
            for bookAd in bookAds:
                diffRecords.append(getattr(bookAd.getSeller(), record))
        elif (record.lower() == "price") or (record.lower() == "condition") or (record.lower() == "comment"):
            for bookAd in bookAds:
                diffRecords.append(getattr(bookAd, record))
        else:
            return "Wrong record."
        return set(diffRecords)

    @staticmethod 
    def getSpecificRecordByRecordType(bookAds, record, value):
        value=value.lower()
        records = []
        if record.lower() == "title":
            for bookAd in bookAds:
                if bookAd.getBook().getTitle().lower() == value:
                    records.append(bookAd.getBook().getTitle())
        elif record.lower() == "author":
            for bookAd in bookAds:
                if bookAd.getBook().getAuthor().lower() == value:
                    records.append(bookAd.getBook().getAuthor())
        elif record.lower() == "release date":
            for bookAd in bookAds:
                if bookAd.getBook().getReleaseDate().lower() == value:
                    records.append(bookAd.getBook().getReleaseDate())
        elif record.lower() == "category":
            for bookAd in bookAds:
                if bookAd.getBook().getCategory().lower() == value:
                    records.append(bookAd.getBook().getCategory())
        elif record.lower() == "genre":
            for bookAd in bookAds:
                if bookAd.getBook().getBookType().lower() == value:
                    records.append(bookAd.getBook().getBookType())
        elif record.lower() == "username":
            for bookAd in bookAds:
                if bookAd.getSeller().getUsername().lower() == value:
                    records.append(bookAd.getSeller().getUsername())
        elif record.lower() == "city":
            for bookAd in bookAds:
                if bookAd.getSeller().getUsername().lower() == value:
                    records.append(bookAd.getSeller().getCity())
        elif record.lower() == "price":
            for bookAd in bookAds:
                if bookAd.getSeller().getUsername().lower() == value:
                    records.append(bookAd.getPrice)
        elif record.lower() == "condition":
            for bookAd in bookAds:
                if bookAd.getSeller().getUsername().lower() == value:
                    records.append(bookAd.getCondition)
        elif record.lower() == "comment":
            for bookAd in bookAds:
                if bookAd.getSeller().getUsername().lower() == value:
                    records.append(bookAd.getComment)
        else:
            return "Wrong record."
        return records

    @staticmethod 
    def getBoodAdInfoByRecord(bookAds, record, value):
        value=value.lower()
        records = []
        if record.lower() == "title":
            for bookAd in bookAds:
                if bookAd.getBook().getTitle().lower() == value:
                    records.append(bookAd)
        elif record.lower() == "author":
            for bookAd in bookAds:
                if bookAd.getBook().getAuthor().lower() == value:
                    records.append(bookAd)
        elif record.lower() == "release date":
            for bookAd in bookAds:
                if bookAd.getBook().getReleaseDate().lower() == value:
                    records.append(bookAd)
        elif record.lower() == "category":
            for bookAd in bookAds:
                if bookAd.getBook().getCategory().lower() == value:
                    records.append(bookAd)
        elif record.lower() == "genre":
            for bookAd in bookAds:
                if bookAd.getBook().getBookType().lower() == value:
                    records.append(bookAd)
        elif record.lower() == "username":
            for bookAd in bookAds:
                if bookAd.getSeller().getUsername().lower() == value:
                    records.append(bookAd)
        elif record.lower() == "city":
            for bookAd in bookAds:
                if bookAd.getSeller().getUsername().lower() == value:
                    records.append(bookAd)
        elif record.lower() == "price":
            for bookAd in bookAds:
                if bookAd.getSeller().getUsername().lower() == value:
                    records.append(bookAd)
        elif record.lower() == "condition":
            for bookAd in bookAds:
                if bookAd.getSeller().getUsername().lower() == value:
                    records.append(bookAd)
        elif record.lower() == "comment":
            for bookAd in bookAds:
                if bookAd.getSeller().getUsername().lower() == value:
                    records.append(bookAd)
        else:
            return "Wrong record."
        return records

    @staticmethod 
    def changeBookAdInfoByRecord(bookAds, record, value, newValue):
        value=value.lower()
        if record.lower() == "title":
            for bookAd in bookAds:
                if bookAd.getBook().getTitle().lower() == value:
                    bookAd.getBook().changeTitle(newValue)
        elif record.lower() == "author":
            for bookAd in bookAds:
                if bookAd.getBook().getAuthor().lower() == value:
                    bookAd.getBook().changeAuthor(newValue)
        elif record.lower() == "release date":
            for bookAd in bookAds:
                if bookAd.getBook().getReleaseDate().lower() == value:
                    bookAd.getBook().changeReleaseDate(newValue)
        elif record.lower() == "username":
            for bookAd in bookAds:
                if bookAd.getSeller().getUsername().lower() == value:
                    bookAd.getSeller().changeUsername(newValue)
        elif record.lower() == "city":
            for bookAd in bookAds:
                if bookAd.getSeller().getUsername().lower() == value:
                    bookAd.getSeller().changeCity(newValue)
        elif record.lower() == "price":
            for bookAd in bookAds:
                if bookAd.getSeller().getUsername().lower() == value:
                    bookAd.getPrice().changePrice(newValue)
        elif record.lower() == "condition":
            for bookAd in bookAds:
                if bookAd.getSeller().getUsername().lower() == value:
                    bookAd.getCondition().changeCondition(newValue)
        elif record.lower() == "comment":
            for bookAd in bookAds:
                if bookAd.getSeller().getUsername().lower() == value:
                    bookAd.getComment().changeComment(newValue)
        else:
            return "Wrong record."
        return "Changed."

    @staticmethod 
    def getBookAdsByYear(bookAds, choice, year):
        bookAdsList = []
        if choice.lower() == "older" :
            for oneBookAd in bookAds:
                if int(oneBookAd.getBook().getReleaseDate())<year:
                    bookAdsList.append(oneBookAd)
        elif choice.lower() == "newer" :
            for oneBookAd in bookAds:
                if int(oneBookAd.getBook().getReleaseDate())>year:
                    bookAdsList.append(oneBookAd)
        elif choice.lower() == "equal" :
            for oneBookAd in bookAds:
                if int(oneBookAd.getBook().getReleaseDate())==year:
                    bookAdsList.append(oneBookAd)
        else:
            return "Wrong choice selected."
        return bookAdsList

    @staticmethod 
    def getBookAdsByPrice(bookAds, choice, price):
        bookAdsList = []
        if choice.lower() == "lower" :
            for oneBookAd in bookAds:
                if float(oneBookAd.getPrice())<price:
                    bookAdsList.append(oneBookAd)
        elif choice.lower() == "higher" :
            for oneBookAd in bookAds:
                if float(oneBookAd.getPrice())>price:
                    bookAdsList.append(oneBookAd)
        elif choice.lower() == "equal" :
            for oneBookAd in bookAds:
                if float(oneBookAd.getPrice())==price:
                    bookAdsList.append(oneBookAd)
        else:
            return "Wrong choice selected."
        return bookAdsList
